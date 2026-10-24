import json, math, random, colorsys, sys
N = 48
def area2(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def poly_area(p): return sum(p[i][0]*p[(i+1)%len(p)][1]-p[(i+1)%len(p)][0]*p[i][1] for i in range(len(p)))/2
def inside(pt,a,b,c):
    d1=area2(a,b,pt); d2=area2(b,c,pt); d3=area2(c,a,pt)
    return (d1>0 and d2>0 and d3>0) or (d1<0 and d2<0 and d3<0)
def earclip(pts):
    p=list(pts)
    if poly_area(p)<0: p=p[::-1]   # make CCW in math sense (y-down => visually CW, irrelevant)
    idx=list(range(len(p))); tris=[]
    guard=0
    while len(idx)>3 and guard<10000:
        guard+=1; found=False
        for k in range(len(idx)):
            i0,i1,i2=idx[k-1],idx[k],idx[(k+1)%len(idx)]
            a,b,c=p[i0],p[i1],p[i2]
            if area2(a,b,c)<=1e-9: continue
            if any(inside(p[j],a,b,c) for j in idx if j not in (i0,i1,i2)): continue
            tris.append((i0,i1,i2)); idx.pop(k); found=True; break
        if not found: raise Exception("earclip failed")
    tris.append(tuple(idx))
    return p,tris
def incircle(a,b,c,d):
    # a,b,c CCW (area2>0); >0 if d inside circumcircle
    ax,ay=a[0]-d[0],a[1]-d[1]; bx,by=b[0]-d[0],b[1]-d[1]; cx,cy=c[0]-d[0],c[1]-d[1]
    return (ax*ax+ay*ay)*(bx*cy-cx*by)-(bx*bx+by*by)*(ax*cy-cx*ay)+(cx*cx+cy*cy)*(ax*by-bx*ay)
def flips(p,tris):
    tris=[list(t) for t in tris]
    for _ in range(200):
        changed=False
        edges={}
        for ti,t in enumerate(tris):
            for k in range(3):
                e=tuple(sorted((t[k],t[(k+1)%3]))); edges.setdefault(e,[]).append(ti)
        for e,ts in edges.items():
            if len(ts)!=2: continue
            t1,t2=tris[ts[0]],tris[ts[1]]
            o1=[v for v in t1 if v not in e][0]; o2=[v for v in t2 if v not in e][0]
            a,b=e
            A,B,C=p[a],p[b],p[o1]
            if area2(A,B,C)<0: A,B=B,A
            if incircle(A,B,C,p[o2])>1e-9:
                # convexity check: new tris (o1,o2,a) and (o1,o2,b) must have opposite orientation sides
                s1=area2(p[o1],p[o2],p[a]); s2=area2(p[o1],p[o2],p[b])
                if s1*s2<0:
                    tris[ts[0]]=[o1,o2,a]; tris[ts[1]]=[o1,o2,b]; changed=True; break
        if not changed: break
    return [tuple(t) for t in tris]
def tri_area(t): return abs(area2(*t))/2
def hex2rgb(h): h=h.lstrip('#'); return [int(h[i:i+2],16)/255 for i in (0,2,4)]
def rgb2hex(c): return '#'+''.join('%02x'%max(0,min(255,round(v*255))) for v in c)
def mix(cols,t):
    t=max(0,min(1,t)); n=len(cols)-1; k=min(int(t*n),n-1); f=t*n-k
    a,b=hex2rgb(cols[k]),hex2rgb(cols[k+1]); return [a[i]+(b[i]-a[i])*f for i in range(3)]
def build(nombre, partes, seed):
    rnd=random.Random(seed); out=[]
    for parte in partes:
        pts=[tuple(map(float,q)) for q in parte['pts']]
        if len(pts)==3: p,tris=pts,[(0,1,2)]
        else:
            p,tris=earclip(pts); tris=flips(p,tris)
        parte['z']=partes.index(parte)
        for t in tris: out.append({'t':[p[i] for i in t],'parte':parte})
    base=len(out)
    while len(out)<N:
        # bisect largest (area weighted by part weight) triangle at longest edge
        k=max(range(len(out)),key=lambda i: tri_area(out[i]['t'])*out[i]['parte'].get('peso',1))
        a,b,c=out[k]['t']
        es=[(a,b,c),(b,c,a),(c,a,b)]
        u,v,w=max(es,key=lambda e:(e[0][0]-e[1][0])**2+(e[0][1]-e[1][1])**2)
        m=((u[0]+v[0])/2,(u[1]+v[1])/2)
        parte=out[k]['parte']; out.pop(k)
        out.append({'t':[u,m,w],'parte':parte}); out.append({'t':[m,v,w],'parte':parte})
    if len(out)>N: raise Exception(f"{nombre}: {len(out)} > {N}")
    # colors
    piezas=[]
    for o in out:
        t=o['t']; parte=o['parte']
        cx=sum(q[0] for q in t)/3; cy=sum(q[1] for q in t)/3
        xs=[q[0] for q in parte['pts']]; ys=[q[1] for q in parte['pts']]
        g=parte.get('grad',('lin',0,1))
        if g[0]=='lin':
            dx,dy=g[1],g[2]
            proj=[x*dx+y*dy for x,y in zip(xs,ys)]; lo,hi=min(proj),max(proj)
            tt=((cx*dx+cy*dy)-lo)/((hi-lo) or 1)
        else:
            _,ox,oy,r=g; tt=math.hypot(cx-ox,cy-oy)/r
        rgb=mix(parte['col'],tt)
        h,l,s=colorsys.rgb_to_hls(*rgb)
        l=max(0,min(1,l+rnd.uniform(-1,1)*parte.get('jit',0.05)))
        rgb=colorsys.hls_to_rgb(h,l,s)
        # expand slightly to hide seams
        e=0.35
        tt2=[]
        for q in t:
            dx,dy=q[0]-cx,q[1]-cy; d=math.hypot(dx,dy) or 1
            tt2.append((round(q[0]+dx/d*e,2),round(q[1]+dy/d*e,2)))
        piezas.append({'p':tt2,'c':rgb2hex(rgb),'cx':cx,'cy':cy,'z':parte['z']})
    # order pieces by angle around figure centre -> coherent morphs
    mx=sum(q['cx'] for q in piezas)/N; my=sum(q['cy'] for q in piezas)/N
    piezas.sort(key=lambda q: math.atan2(q['cy']-my,q['cx']-mx))
    print(nombre,'base',base,'->',len(piezas),file=sys.stderr)
    return [[*[c for q in pz['p'] for c in q], pz['c'], pz['z']] for pz in piezas]

def espejo(pts): return [(100-x,y) for x,y in pts][::-1]

ceiba=[
 {'pts':[(46,50),(54,50),(55,68),(58,79),(67,88),(56,87),(52,82),(50,89),(48,82),(44,87),(33,88),(42,79),(45,68)],
  'col':['#8a6a4a','#5b4130','#3b2a1f'],'grad':('lin',0,1),'jit':.06},
 {'pts':[(46,52),(40,46),(34,44),(36,42),(43,44),(48,48)],'col':['#6b5038','#4a3626'],'jit':.04},
 {'pts':[(54,52),(60,46),(67,43),(66,41),(58,44),(52,48)],'col':['#6b5038','#4a3626'],'jit':.04},
 {'pts':[(12,45),(16,37),(25,32),(30,26),(40,23),(47,17),(56,18),(62,23),(72,24),(79,30),(87,35),(89,44),(80,48),(68,49),(60,46),(50,49),(40,46),(30,49),(20,49)],
  'col':['#b9dd78','#62b05a','#2f7a46','#1d5236'],'grad':('lin',0.25,1),'jit':.07,'peso':1.15},
]
colibri=[
 {'pts':[(5,34),(31,38.5),(31,41.5)],'col':['#c8ccc4','#9aa39b'],'jit':.02},
 {'pts':[(48,40),(46,27),(48,15),(54,7),(58,11),(57,24),(55,37)],'col':['#7fa8d6','#33507a'],'grad':('lin',0,1),'jit':.06},
 {'pts':[(44,42),(50,30),(58,20),(68,12),(80,5),(85,8),(81,18),(73,30),(63,42),(55,48)],'col':['#a9c9ec','#5c86c0','#2d4a7c'],'grad':('lin',-1,1),'jit':.07},
 {'pts':[(30,41),(32,35),(37,32.5),(42,34),(46,39),(54,45),(62,53),(67,60),(64,64),(56,62),(48,58),(40,52),(33,47)],
  'col':['#6ef0b0','#24b58a','#0f7d6b','#0d5a58'],'grad':('lin',1,1),'jit':.07},
 {'pts':[(32,44),(37,47),(43,52),(38,51),(33,47.5)],'col':['#ff4f9a','#c2236a'],'jit':.05},
 {'pts':[(35.2,37.2),(38.4,36.2),(37.6,39.2)],'col':['#0a1a1e','#0a1a1e'],'jit':.0},
 {'pts':[(61,55),(68,59),(83,71),(75,72.5),(73,83),(64,66)],'col':['#14806f','#1e3f5c'],'grad':('lin',1,1),'jit':.06},
]
def fronda(bx,by,ang,L,w,arco,caida):
    a=math.radians(ang); dx,dy=math.cos(a),math.sin(a); nx,ny=-dy,dx
    mx,my=bx+dx*L*.55,by+dy*L*.55-arco
    tip=(bx+dx*L,by+dy*L+caida)
    return [(bx,by),(mx+nx*w,my+ny*w),tip,(mx-nx*w,my-ny*w)]
hoja=['#4f9a68','#2f6e4b','#1f4d36']
hoja_lejos=['#7c988c','#5d7a70']
palma=[
 {'pts':[(28,90.5),(33,90.5),(32.2,62),(31.6,47),(30.4,47),(29.6,62)],'col':['#8d9c96','#b3beb7'],'grad':('lin',0,-1),'jit':.05,'peso':1.6},
]
for ang,L,ar,ca in [(-150,19,4,9),(-112,16,3,3),(-70,16,3,3),(-32,19,4,9),(178,16,1,11)]:
    palma.append({'pts':fronda(31,46.5,ang,L,2.8,ar,ca),'col':hoja_lejos,'grad':('lin',math.cos(math.radians(ang)),math.sin(math.radians(ang))),'jit':.05})
palma.append({'pts':[(22,92),(38,89.5),(70,89),(84,92),(52,94)],'col':['#4b5a50','#33403a'],'grad':('lin',0,1),'jit':.05})
palma.append({'pts':[(49.2,91),(55.6,91),(55,62),(54.2,33),(53,29.5),(51.6,33),(50.4,62)],'col':['#e6ebe2','#c4ccc2','#a8b3aa'],'grad':('lin',0,1),'jit':.09,'peso':3.2})
for ang,L,ar,ca in [(-165,33,9,17),(-132,30,8,8),(-98,26,5,2),(-60,30,8,8),(-22,33,9,17),(168,28,3,22),(14,28,3,22)]:
    palma.append({'pts':fronda(53,30,ang,L,4.4,ar,ca),'col':hoja,'grad':('lin',math.cos(math.radians(ang)),math.sin(math.radians(ang))),'jit':.07,'peso':1.3})
cuerpo=[(50,23),(58,25),(64,31),(66,42),(66,56),(62,66),(56,72),(50,73),(44,72),(38,66),(34,56),(34,42),(36,31),(42,25)]
pata_d=[(36,46),(24,42),(18,34),(11,31),(16,28),(14,21),(20,27),(26,32),(36,40)]
pata_t=[(38,58),(24,54),(16,60),(18,70),(13,80),(20,78),(22,87),(26,76),(24,66),(38,68)]
oro=['#ffe27a','#ffc233','#f29d12']
oro_p=['#ffd25a','#eaa21c','#bf6a08']
rana=[
 {'pts':pata_d,'col':oro_p,'grad':('lin',-1,0),'jit':.06},
 {'pts':espejo(pata_d),'col':oro_p,'grad':('lin',1,0),'jit':.06},
 {'pts':pata_t,'col':oro_p,'grad':('lin',-1,0.5),'jit':.06},
 {'pts':espejo(pata_t),'col':oro_p,'grad':('lin',1,0.5),'jit':.06},
 {'pts':cuerpo,'col':oro,'grad':('rad',50,40,34),'jit':.06,'peso':1.1},
 {'pts':[(35,31),(39,24),(46,25.5),(44,32),(39,34)],'col':['#3a2508','#1e1405'],'jit':.03},
 {'pts':espejo([(35,31),(39,24),(46,25.5),(44,32),(39,34)]),'col':['#3a2508','#1e1405'],'jit':.03},
]
jaguar=[
 {'pts':[(64,58),(70,58),(69,68),(70,79),(65,80.5),(64.5,68)],'col':['#a8722e','#7c4f1d'],'grad':('lin',0,1),'jit':.05},
 {'pts':[(26,36),(50,35),(74,37),(80,40),(84,44),(90,50),(93,62),(90,66),(88,56),(83,49),(82,53),(79,66),(81,79),(75,82),(73,68),(71,60),(60,59),(48,59),(44,64),(44,80),(38,82),(37,70),(36,62),(31,70),(24,80),(19,79),(26,62),(25,50)],
  'col':['#f2c063','#e09a3c','#c9822f','#ead7a8'],'grad':('lin',0,1),'jit':.06,'peso':1.2},
 {'pts':[(28,36),(25,31),(22,30.5),(19,32),(14,34),(9,38),(7,43),(9,47),(14,50),(22,51),(28,48)],'col':['#f0bc5c','#dd9a3e','#f1ddb0'],'grad':('lin',-0.3,1),'jit':.06},
 {'pts':[(13.4,38.6),(16.4,38.4),(15,40.4)],'col':['#1d1408','#1d1408'],'jit':0},
]
for x,y,r,g in [(36,43,1.8,0),(46,40,2,1),(57,41,2.1,2),(67,42,2,3),(75,49,1.9,4),(52,50,1.9,5),(63,51,1.8,6),(40,52,1.8,7)]:
    a=g*1.7
    jaguar.append({'pts':[(x+math.cos(a+k*2.09)*r,y+math.sin(a+k*2.09)*r) for k in range(3)],'col':['#3b230f','#4a2c13'],'jit':.04})
azul=['#7fd6ff','#2f8cff','#1a4fd8','#0b1f66']
ala_a=[(48,44),(40,30),(30,20),(18,13),(7,15),(5,26),(11,38),(24,46),(40,48)]
ala_p=[(48,50),(38,50),(24,54),(15,64),(17,77),(28,85),(38,83),(46,71),(49,58)]
morpho=[
 {'pts':ala_a,'col':azul,'grad':('rad',50,47,46),'jit':.07,'peso':1.1},
 {'pts':espejo(ala_a),'col':azul,'grad':('rad',50,47,46),'jit':.07,'peso':1.1},
 {'pts':ala_p,'col':azul,'grad':('rad',50,50,42),'jit':.07},
 {'pts':espejo(ala_p),'col':azul,'grad':('rad',50,50,42),'jit':.07},
 {'pts':[(49,36),(51,36),(52.2,46),(51.6,68),(50,73),(48.4,68),(47.8,46)],'col':['#3b2f2a','#1b1512'],'grad':('lin',0,1),'jit':.04},
 {'pts':[(49.3,37),(43,20),(44.4,19.6)],'col':['#4a3c35','#4a3c35'],'jit':.02},
 {'pts':[(50.7,37),(55.6,19.6),(57,20)],'col':['#4a3c35','#4a3c35'],'jit':.02},
]
res={
 'ceiba':build('ceiba',ceiba,1),'colibri':build('colibri',colibri,2),'palma':build('palma',palma,3),
 'jaguar':build('jaguar',jaguar,4),'morpho':build('morpho',morpho,5)}
print(json.dumps(res,separators=(',',':')))

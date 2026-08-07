class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)

        tt = t
        need2 = need3 = need5 = need7 = 0
        while tt % 2 == 0: tt //= 2; need2 += 1
        while tt % 3 == 0: tt //= 3; need3 += 1
        while tt % 5 == 0: tt //= 5; need5 += 1
        while tt % 7 == 0: tt //= 7; need7 += 1
        if tt != 1:
            return "-1"

        dig_e = {1:(0,0,0,0),2:(1,0,0,0),3:(0,1,0,0),4:(2,0,0,0),5:(0,0,1,0),
                  6:(1,1,0,0),7:(0,0,0,1),8:(3,0,0,0),9:(0,2,0,0)}

        amax, bmax = need2, need3
        cnt23 = [[0]*(bmax+1) for _ in range(amax+1)]
        for i in range(amax+1):
            for j in range(bmax+1):
                if i == 0 and j == 0:
                    continue
                best = None
                for e2,e3,e5,e7 in dig_e.values():
                    if e2 == 0 and e3 == 0:
                        continue
                    ni, nj = max(0, i-e2), max(0, j-e3)
                    if ni == i and nj == j:
                        continue
                    val = 1 + cnt23[ni][nj]
                    if best is None or val < best:
                        best = val
                cnt23[i][j] = best

        def minCount(r2, r3, r5, r7):
            return r5 + r7 + cnt23[min(r2, amax)][min(r3, bmax)]

        def buildCore(r2, r3, r5, r7, K):
            res = []
            cr2, cr3, cr5, cr7 = r2, r3, r5, r7
            rem = K
            for _ in range(K):
                rem -= 1
                for digit in range(1, 10):
                    e2,e3,e5,e7 = dig_e[digit]
                    nr2,nr3,nr5,nr7 = max(0,cr2-e2), max(0,cr3-e3), max(0,cr5-e5), max(0,cr7-e7)
                    if minCount(nr2,nr3,nr5,nr7) <= rem:
                        res.append(str(digit))
                        cr2,cr3,cr5,cr7 = nr2,nr3,nr5,nr7
                        break
            return ''.join(res)

        P2=[0]*(n+1); P3=[0]*(n+1); P5=[0]*(n+1); P7=[0]*(n+1)
        z = None
        for i, ch in enumerate(num):
            di = int(ch)
            if di == 0:
                if z is None: z = i
                P2[i+1],P3[i+1],P5[i+1],P7[i+1] = P2[i],P3[i],P5[i],P7[i]
            else:
                e2,e3,e5,e7 = dig_e[di]
                P2[i+1]=P2[i]+e2; P3[i+1]=P3[i]+e3; P5[i+1]=P5[i]+e5; P7[i+1]=P7[i]+e7

        if z is None and P2[n]>=need2 and P3[n]>=need3 and P5[n]>=need5 and P7[n]>=need7:
            return num

        p_start = z if z is not None else n-1

        for p in range(p_start, -1, -1):
            pe2,pe3,pe5,pe7 = P2[p],P3[p],P5[p],P7[p]
            for dd in range(int(num[p])+1, 10):
                e2,e3,e5,e7 = dig_e[dd]
                te2,te3,te5,te7 = pe2+e2, pe3+e3, pe5+e5, pe7+e7
                r2,r3,r5,r7 = max(0,need2-te2), max(0,need3-te3), max(0,need5-te5), max(0,need7-te7)
                L = n-1-p
                K = minCount(r2,r3,r5,r7)
                if K <= L:
                    core = buildCore(r2,r3,r5,r7,K)
                    return num[:p] + str(dd) + '1'*(L-K) + core

        K_full = minCount(need2, need3, need5, need7)
        Lp = max(n+1, K_full)
        core = buildCore(need2, need3, need5, need7, K_full)
        return '1'*(Lp-K_full) + core
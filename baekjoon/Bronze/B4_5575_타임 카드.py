A_h, A_m, A_s, A_h_e, A_m_e, A_s_e = map(int, input().split())
B_h, B_m, B_s, B_h_e, B_m_e, B_s_e = map(int, input().split())
C_h, C_m, C_s, C_h_e, C_m_e, C_s_e = map(int, input().split())

A_total = (A_s_e + (A_m_e*60) + (A_h_e*3600)) - (A_s + (A_m*60) + (A_h*3600))
B_total = (B_s_e + (B_m_e*60) + (B_h_e*3600)) - (B_s + (B_m*60) + (B_h*3600))
C_total = (C_s_e + (C_m_e*60) + (C_h_e*3600)) - (C_s + (C_m*60) + (C_h*3600))

AH = A_total // 3600
AM = (A_total-(AH*3600)) // 60
AS = A_total-(AH*3600)-(AM*60)

BH = B_total // 3600
BM = (B_total-(BH*3600)) // 60
BS = B_total-(BH*3600)-(BM*60)

CH = C_total // 3600
CM = (C_total-(CH*3600)) // 60
CS = C_total-(CH*3600)-(CM*60)


print(AH, AM, AS)
print(BH, BM, BS)
print(CH, CM, CS)
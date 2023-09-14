import cv2
anh1=cv2.imread('./xu ly anh/data/3.png')
anh2=cv2.imread('./xu ly anh/data/4.png')
if anh1.shape[1]<anh2.shape[1]:
    anh2=cv2.resize(anh2, (anh1.shape[1],anh1.shape[0]))
else:
    anh1=cv2.resize(anh1, (anh2.shape[1],anh2.shape[0]))
anhketqua=cv2.addWeighted(anh1,0.8, anh2, 0.2, 30)
cv2.imshow('anh ket qua',anhketqua)
cv2.waitKey()
cv2.destroyAllWindows()
    

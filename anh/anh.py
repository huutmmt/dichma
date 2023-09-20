import cv2
import numpy as np

#Vẽ hình chữ nhật dựa trên vùng đã chọn
def draw_rectangle(event, x, y, flags, params):
    global x_init, y_init, drawing, top_left_pt, bottom_right_pt,img_orig,bd
    #Phát hiện sự kiện nhấn chuột trái
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_init, y_init = x, y
    
    #Phát hiện di chuyển chuột
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)
            img[y_init:y, x_init:x] = 255 - img_orig[y_init:y,x_init:x]
            cv2.rectangle(img, top_left_pt, bottom_right_pt,(0,255,0), 2)
    
    #Phát hiện sự kiện thả chuột trái
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        top_left_pt, bottom_right_pt = (x_init,y_init), (x,y)
        img[y_init:y, x_init:x] = 255 - img[y_init:y, x_init:x]
        cv2.rectangle(img, top_left_pt, bottom_right_pt,
        (0,255,0), 2)
        rect_final = (x_init, y_init, x-x_init, y-y_init)   
    #Chạy Grabcut trên vùng quan tâm ROI (region of interest)
    run_grabcut(img_orig, rect_final)        
    
#Giải thuật Grabcut
def run_grabcut(img_orig, rect_final):
    anhgoc=img_orig.copy()
    nen=cv2.imread('data/dep.jpg')
    nen=cv2.resize(nen, (img_orig.shape[1],img_orig.shape[0]))
    # Initialize the mask
    mask = np.zeros(img_orig.shape[:2],np.uint8)
    # Extract the rectangle and set the region of
    # interest in the above mask
    x,y,w,h = rect_final
    mask[y:y+h, x:x+w] = 1
    # Initialize background and foreground models
    bgdModel = np.zeros((1,65), np.float64)
    fgdModel = np.zeros((1,65), np.float64)
    # Run Grabcut algorithm
    cv2.grabCut(img_orig, mask, rect_final, bgdModel, fgdModel,
                5, cv2.GC_INIT_WITH_RECT)
    # Extract new mask
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    cv2.imshow('mask',mask2*255)
    # Tạo ảnh kết quả thay nền mới
    img_orig = img_orig*mask2[:,:,np.newaxis]+ nen* (1 - mask2[:, :, np.newaxis])
    # Trường hợp khác
    anhketqua=cv2.bitwise_and(anhgoc,nen,mask=mask2)
    cv2.imshow('ghep anh',anhketqua)
    cv2.imshow('ghep nen',img_orig)
if __name__=='__main__':
    drawing = False
    top_left_pt, bottom_right_pt = (-1,-1), (-1,-1)
    # Read the input image
    img_orig = cv2.imread('image/meo.jpg')
    img = img_orig.copy()
    cv2.namedWindow('Input')
    cv2.setMouseCallback('Input', draw_rectangle)
    while True:
        cv2.imshow('Input', img)
        c = cv2.waitKey(1)
        if c == 27:
            break
    cv2.destroyAllWindows()
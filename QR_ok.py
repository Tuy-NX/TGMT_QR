import qrcode
import cv2

print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
TT = input()
while(1):
    if TT == '1':
        print("Tạo QR Code.")
        print("Nhập data QR-Code.")
        data=input()
        print("Nhập tên QR-Code.")
        name=input()+'.png'
        img = qrcode.make(data)
        img.save(name)
        print("Tạo QR-Code thành công. ")
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
        TT = input()

    if TT=='2':
        name=input()+'.png'
        img = cv2.imread(name)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        if bbox is not None:
            print(f"QRCode data: {data}")
            n_lines = len(bbox)
            for i in range(n_lines):
                point1 = tuple(bbox[i][0])
                point2 = tuple(bbox[(i+1) % n_lines][0])

        cv2.imshow("QR_Code", img)
        while(1):
            if cv2.waitKey(0) == ord("q"):
                break
        cv2.destroyAllWindows()       
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera. \n 4: Thoát.")
        TT = input()

    if TT=='3':
   
        cap = cv2.VideoCapture(0)
        detector = cv2.QRCodeDetector()
        while True:
            _, img = cap.read()
            data, bbox, _ = detector.detectAndDecode(img)
            if bbox is not None:
                    bb_pts = bbox.astype(int).reshape(-1, 2)
                    num_bb_pts = len(bb_pts)
                    for i in range(num_bb_pts):
                        cv2.line(img,
                            tuple(bb_pts[i]),
                            tuple(bb_pts[(i+1) % num_bb_pts]),
                            color=(255, 0, 255), thickness=2)
                        cv2.putText(img, data,
                            (bb_pts[0][0], bb_pts[0][1] - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (0, 255, 0), 2)
            if data:
                        
                        print("Phát hiện mã QRCode có data là:", data)

            else:
                        print("Không phát hiện hoặc không đọc được mã QR")

            cv2.imshow("Camera", img)    
            if cv2.waitKey(1) == ord("q"):
                break
        cap.release()
        cv2.destroyAllWindows()
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera. \n 4: Thoát.")
        TT = input()

    if TT=='4':
        break
    else:
        print("Nhập lựa chọn:\n 1: Tạo QR-Code. \n 2: Quét QR-Code bằng ảnh. \n 3: Quét QR-Code bằng camera.\n 4: Thoát.")
        TT = input()



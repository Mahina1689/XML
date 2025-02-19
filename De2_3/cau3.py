from xml.dom import minidom
import pandas as pd


def load(file):
        doc = minidom.parse(file)
        return doc
       


def luu(doc, file):
    with open(file, "w", encoding="utf-8") as f:
        doc.writexml(f, addindent="\t", newl="\n", encoding="utf-8")
    print(f"Tệp đã luu ")


def hienthi(doc):

    root = doc.documentElement
    data = []
    for nv in root.getElementsByTagName("nvda"):
        manv = nv.getElementsByTagName("manv")[0].firstChild.data
        ten = nv.getElementsByTagName("mada")[0].firstChild.data
        ns = nv.getElementsByTagName("date")[0].firstChild.data
        dc = nv.getElementsByTagName("danhgia")[0].firstChild.data
        data.append([manv, ten, ns,dc])
    df = pd.DataFrame(data, columns=["mã nhân viên", "mã nhân viên", "ngày nghiệm thu", "đánh giá"])
    print(df)


def them(doc, file, mada, manv, date, dg,):
   

    root = doc.documentElement
    new_da = doc.createElement("nvda")

    mada_elem = doc.createElement("mada")
    mada_elem.appendChild(doc.createTextNode(mada))
    new_da.appendChild(mada_elem)

    manv_elem = doc.createElement("manv")
    manv_elem.appendChild(doc.createTextNode(manv))
    new_da.appendChild(manv_elem)

    date_elem = doc.createElement("date")
    date_elem.appendChild(doc.createTextNode(date))
    new_da.appendChild(date_elem)
    
    dg_elem = doc.createElement("danhgia")
    dg_elem.appendChild(doc.createTextNode(dg))
    new_da.appendChild(dg_elem)

    root.appendChild(new_da)
    luu(doc, file)


def sua(doc, file, mada, new_nv, new_date, new_dg):

    root = doc.documentElement
    for nv in root.getElementsByTagName("nvda"):
        manv_elem = nv.getElementsByTagName("mada")[0]
        if manv_elem.firstChild.data == mada:
            nv.getElementsByTagName("manv")[0].firstChild.replaceWholeText(new_nv)
            nv.getElementsByTagName("date")[0].firstChild.replaceWholeText(str(new_date))
            nv.getElementsByTagName("danhgia")[0].firstChild.replaceWholeText(new_dg)
       
            print(f"Đã cập nhật dự án {mada}.")
            luu(doc, file)
            return
    print(f"dự án với mã {mada} không tìm thấy.")


def xoa(doc, filepath, mada):


    root = doc.documentElement
    for nv in root.getElementsByTagName("nvda"):
        manv_elem = nv.getElementsByTagName("mada")[0]
        if manv_elem.firstChild.data == mada:
            root.removeChild(nv)
            print(f"Đã xóa dự án {mada}.")
            luu(doc, filepath)
            return
    print(f"dự án {mada} không tồn tại.")


def menu():
    filepath = r'D:\xml\cau2duan\thamgia.xml'

    doc = load(filepath)

    while True:
        print("\n--- Menu ---")
        print("1. Thêm dự án")
        print("2. Sửa dự án")
        print("3. Xóa  ")
        print("4. Hiển thị ")
        print("5. Thoát")

        choice = input("Nhập lựa chọn của bạn: ")
        if choice == "1":
            mada = input("Nhập mã dự án: ")
            manv = input("Nhập mã nhân viên : ")
            date = input("Nhập ngày ngày nghiêm thu: ")
            dg = input("Nhập đánh gia : ")
           
            them(doc, filepath, mada, manv, date, dg)
        elif choice == "2":
            mada = input("Nhập mã dự án: ")
            manv = input("Nhập mã nhân viên : ")
            date = input("Nhập ngày ngày nghiêm thu: ")
            dg = input("Nhập đánh gia : ")
           
            sua(doc, filepath, mada, manv, date, dg)
        elif choice == "3":
            mada = input("Nhập mã dự án muốn xóa: ")
            xoa(doc, filepath, mada)
        elif choice == "4":
            print("\nDanh sách dự án:")
            hienthi(doc)
        elif choice == "5":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    print("Đang chạy...")
    menu()

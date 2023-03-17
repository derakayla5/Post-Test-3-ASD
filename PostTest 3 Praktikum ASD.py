class Node:
      # constructor for Node class
        def __init__(self, data):
            self.data = data
            self.ref = None

class TicketLists():
      # constructor for LinkedList class
        def __init__(self):
            self.head = None
        
        def tampil(self):
            if self.head is None:
                print("Data tidak tersedia")
            
            else:
                n = self.head
                while n is not None:
                    print(n.data, end=" <--- ")
                    n = n.ref
        
        def tambahtiket(self, data):
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node

        def hapustiket(self):
            if self.head is None:
                print("Kosong")
            else:
                self.head = self.head.ref

ticket_list = TicketLists()

while True:
    print("\nWelcome to the Blackpink concert ticket booking system!")
    print("1. Tambah data kursi")
    print("2. Lihat Susunan Kursi")
    print("3. Hapus Kursi")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        ticket_number = input("Masukan kode kursi : ")
        ticket_list.tambahtiket(ticket_number)
        print("Data berhasil ditambahkan")
        
    elif choice == 2:
        print("Berikut Data yang sudah diinput :")
        ticket_list.tampil()
        print("\nThank you for Purchasing the Blackpink concert ticket!")
        
    elif choice == 3:
        ticket_list.hapustiket()
        print("Data Berhasil dihapus")
        ticket_list.tampil()
        print("\n")
        
    
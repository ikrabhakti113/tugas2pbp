Link Heroku : https://tugas2pbpikra.herokuapp.com/katalog/

**1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**
![Bagan Framework berbasis DJango](https://user-images.githubusercontent.com/87271057/190218073-4d1582ca-8ebe-4771-af8e-fc956fa86071.png)
User ketika mengakses akan memberikan sebuah client request yang akan diterima oleh url (urls.py) lalu request diteruskan ke view (views.py) yang kemudian melakukan pemrosesan terhadap client request yang masuk. Apabila kasusnya terdapat proses yang membutuhkan data dari database, maka akan mengirimkan data untuk memanggil query yang nantinya akan dikembalikan database dan diteruskan ke views. Jika client request sudah selesai diproses, maka hasil proses akan dipetakan menuju ke templates (berkas html) yang akan diperlihatkan di tampilan web ke user.

**2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Kita memakai Virtual Environment atau env agar proyek yang sedang kita kerjakan tidak bertabrakan dengan versi lain yang ada misalnya ada beberapa proyek yang berjalan dalam satu sistem, maka Virtual Environtment sangat baik dalam isolasi proyek-proyek tersebut. Bayangkan kita tidak menggunakan env pada web berbasis Django, maka setiap update dan dependencies baru akan mengganggu versi proyek yang sedang berjalan dan dengan env lah,kita bisa melakukan update tanpa menggangu versi yang sedang berjalan.

**3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

**Fungsi views.py**

Disini, views akan mengambil semua data-data yang ada di database. Lalu views juga akan menambahkan variabel seperti pada tugas 2 ini nama dan npm yang selanjutnya akana disimpan dalam variabel context dan nantinya dirender dengan memanggil function yang kita buat yaitu show_katalog sehingga dapat dimunculkan datanya pada halaman HTML.

**Routing**

Pada bagian ini, urls.py akan melakukan routing terhadap fungsi yang kita buat show_katalog sehingga halaman HTML bisa terlihat lewat browser.Di bagian ini tak lupa mendaftarkan alamat path sub-aplikasi “katalog” ke dalam urls.py yang ada pada folder project_django.

**Pemetaan **

Pada pemetaan, kita menggunakan for loop untuk mengiterasi data-data yang terdapat pada database yang akan disimpan kedalam variabel list_barang dan terjadilah pemetaan data template.

**Deployment**

DI tahap ini, yang saya lakukan adalah membuka situs heroku da membuat aplikasi baru bernama tugas2pbpikra, dimana selanjutnya ada pilihan connect ke github dan setelah itu kita bisa menyambungkan repository spesifik yang ingin kita deplot, pada kasus ini repo nya bernama tugas2pbp, dan setelah tersambung, akan ada pilihan manual deployment dari heroku, ketika kita klik, aplikasi kita akan terdaftar di World Wide Web dan bisa diakses oleh semua orang!




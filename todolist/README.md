Link : http://tugas2pbpikra.herokuapp.com/

##  Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?

CSRF token berguna untuk membandingkan dua token yang ditemukan pada client side dan server side (request). Jika token tersebut tidak sama maka request pada form akan ditolak, sedangkan jika token sama maka request form akan merespons OK.

Jika tidak terdapat potongan kode CSRF tersebut, maka server akan vulnerable terhadap attach CSRF vulnerabillity, dimana attacker bisa membaut request yang tidak valid ke dalam server backend yang nantinya bisa mengubah struktur backend dan server menjadi terbuka dengan exploit yang lainnya.

## Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.

Bisa, form bisa kita buat secara manual dengan menggunakan method POST dan CSRF token. Lalu kita membuat tag dan didalamnya terdapat tag tr yang digunakan untuk memberikan tag input beserta dengan type field yang disesuaikan dengan kebutuhan data input. Setelah itu, input akan dikembalikan ke fungsi yang melakukan request terhadap form jika form disubmit. Method request.POST.get() nantinya akan digunakan untuk mengakses kembali input client.

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Data inputan user dapat diakses karena adanya penggunaan method request.POST.get(). Lalu dengan method  "Models".objects.create(nama = data input) sesuai denga yang kita buat di todolist/models.py.Nantinya data akan tersimpan pada database django dan bisa diakses menggunakan "Models".objects.filter(user=request.user) yang berguna melakukan filter pada data yang akan masuk hanya data yang sesuai dengan milik inputan user nantinya data akan masuk kedalam context yang di render ke html. Data tadi akan di for-loop pada html agar bisa menampilkan atribut yang ingin ditampilkan.

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Membuat aplikasi todolist dengan python manage.py startapp todolist dan menambahkan todolist pada INSTALLED_APPS di settings.py
2. Menambahkan "path('todolist/', include('todolist.urls'))," pada urls.py di project_django yang sudah terhubung pada fungsi show_todolist di views.py.
3. Membuat model dengan membuat class mytodolistitem pada models.py dan menambahkan field user dengan ForeignKey, date, title, description dan boolean is_finished yang defaultnya false.
4. Membuat fungsi pada views.py untuk meng-implementasi fungsi login, logout, register yang terhubung pada register.html dan login.html dan jangan lupa menambahkan kode @login_required(login_url='/todolist/login/')  diatas fungsi show_todolist agar page todolist hanya bisa diakses jika sudah login.
5. Menambahkan kode "{{user.username}}" untuk menampilkan nama user yang sedang login, lalu menambahkan html button logout dan tambah task dan for-loop untuk menampilkan data tanggal, judul dan deskripsi task.
6. Membuat halaman bernama todolist/create_task untuk men-direct pembuatan task ke page baru yang berisi form untuk meng-input nama task dan deskripsi task yang akan dikirim ke fungsi create_task  di views.py
7. Melakukan routing dengan menambahkan url yang digunakan pada todolist/ kedalam urls.py yang ada didalam file todolist.
8. Deployment automatis karena menggunakan repo github pada tugas sebelumnya yang sudah pernah di-deploy
9. Membuat 2 akun baru pada form registrasi dan masing-masing akan menambahkan 3 data task pada form create_task untuk menambahkan data yang dimiliki masing-masing user.


















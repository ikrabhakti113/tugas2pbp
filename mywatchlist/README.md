Link HEROKU : https://tugas2pbpikra.herokuapp.com/mywatchlist/html/

# 1.Jelaskan perbedaan antara JSON, XML, dan HTML!
JSON (JavaScript Object Notation) digunakan untuk menyimpan dan mengirim data ke aplikasi web ataupun mobile. JSON adalah JavaScript yang berisi key dan value. Bedanya dengan XML dan HTML adalah JSON lebih cepat dan mudah dibaca oleh mesin karena tidak seperti XML dan HTML yang masih menggunakan tag.

XML (Extensible Markup Language) menyimpan elemen-elemennya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, tetapi tidak efisien,dan informasinya dibungkus di dalam tag jadi mudah untuk dibaca.

HTML adalah singkatan dari Hypertext Markup Language, yaitu bahasa markup standar untuk membuat dan menyusun halaman dan aplikasi web. Penggunaan umum HTML adalah untuk menyusun bagian paragraf, heading, maupun link pada halaman web. Tapi, meskipun susunannya seperti coding, HTML bukanlah bahasa pemrograman.

# 2.Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery diperlukan dalam pengimplementasian sebuah platform agar pengerjaan pengiriman data bisa dilakukan dengan mudah. Data delivery menandakan terjadinya pertukaran antara data client dan data di server.  data delivery menggunakan format HTML, JSON, dan XML agar data mudah dipahami oleh bahasa program yang berbeda-beda dan fleksibel dalam dikembangkan oleh pengembang dan bisa dipahami oleh client.

# 3.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

1. Mulai dengan menggunakan command 'python manage.py startapp mywatchlist' untuk membuat/start proyek aplikasi baru didalam repositori yang diinginkan, di cmd.
2. Lalu, lakukan routing ke dalam urls.py dengan menambahkan path ('mywatchlist/', include('mywatchlist.urls')) pada variabel urlpatterns yang ada pada folder project_django agar nantinya HTML dapat ditampilkan lewat browser.
3. Membuat model mywatchlistitem pada mywatchlist/models.py dengan field :
    a. watched_movie
    b. movie_title
    c. movie_rate
    d. release_date
    e. movie_review
   Lalu lakukan perintah 'python manage.py makemigrations' untuk menyiapkan skema model ke database Django pada mesin lokal dan lakkukan perintah 'python manage.py migrate' untuk menerapkan skema ke dalam database Django lokal.
 
4. Jangan lupa menambahkan data yang ingin ditampilkan dengan menggunakan 'initial_watchlist_data.json' yang isinya 10 data yang diminta sebagai isi dari mywatchlistitem dan update PROCFILE dengan command yang melakukan loaddata dengan command 'python manage.py loaddata initial_watchlist_data.json'

5. Membuat fungsi-fungsi pada lab02 seperti fungsi HTML, JSON, XML untuk menyajikan data tersebut dan jangan lupa melakukan routing dengan menambahkan url tersebut pada urls.py.

6. lakukan 4 mantra pull, add, commit dan push lalu deploy ke aplikasi yang terhubung di HEROKU.
   
# POSTMAN

![messageImage_1663788355276](https://user-images.githubusercontent.com/87271057/191655903-50bfd4eb-236c-45f5-8889-2190382d9870.jpg)

![messageImage_1663788391223](https://user-images.githubusercontent.com/87271057/191655918-815444c9-7a53-4a28-97aa-bd6efbe3b60f.jpg)

![messageImage_1663788407895](https://user-images.githubusercontent.com/87271057/191655929-0cb77572-617c-41c3-9398-6e55811d3d64.jpg)




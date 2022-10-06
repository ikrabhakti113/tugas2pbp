# Tugas 5: 

## Nama : Ikra Bhaktiananda
## NPM  : 2106637580
#

### Link Heroku
https://tugas2pbpikra.herokuapp.com/todolist/login/
#

1.	Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

    ### Inline Style CSS : 
    Inline CSS merupakan suatu style yang dapat dituliskan langsung pada atribut HTM. Style yang di tulis langsung pada atribut style. Dapat merubah      secara langsung pada tag HTML sehingga dapat mengupdate CSS secara cepat. 
    Kelebihan dari inline CSS :
        - mampu memperbaiki kode dengan cepat,
        - Proses permintaan HTTP yang lebih kecil sehingga load website akan lebih cepat
        - membantu para web developer ketika ingin menguji dan melihat perubahan pada satu elemen pada tag HTML
    Kekurangan dari inline css:
    Tidak efisien karena hamya diterapkan pada satu line atau tag HTML saja.
    
    
    ### Internal Style CSS:
    merupakan suatu style yang dituliskan pada header file HTML dan kode CSS ditulis di dalam tag <'style>.
     
    Tag <'style> bisa ditulis di dalam tag <'head>, bisa juga ditulis di dalam tag <'body>. Namun Sering sekali menulisnya di dalam <'head>.  Penulisan css di dalam tag <'head> akan lebih dahulu dibaca dibandingkan di <'body>. Karena lebih dahulu dibaca, style yang akan dipakai adalah yang terakhir.

    Kelebihan Internal CSS
    - Perubahan pada Internal CSS hanya berlaku pada satu halaman saja dan tidak perlu menggunakan banyak file eksternal.
    - style hanya terdapat pada 1 page saja jadi page bisa dalam tampilan yang berbeda-beda
    - Class dan ID bisa digunakan oleh internal stylesheet

    Kekurangan Internal CSS:
    - Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
    - Membuat performa website menjadi lambat karena terdapat CSS yang berbeda pada setiap page, codingan yang terlihat berantakan karena menyatukan CSS dan HTML sehingga terlihat terlalu banyak
    
    ### Eksternal Style CSS : 
    adalah suatu style yang dituliskan pada file eksternal (misal: style.css) lalu diimport kedalam file HTML. kemudian cara menghubungkannya ada 2 cara yaitu dengan menggunakan tag <'link> atau dengan @import.

Kelebihan Eksternal CSS: 
- Kode dalam HTML terlihat rapih karena style CSS dituliskan pada file eksternal dan kode HTML juga jadi sedikit sizenya.
- Loading website menjadi lebih cepat.
- File CSS dapat digunakan di beberapa halaman website secara bersamaan.
Kekurangan Internal CSS:
Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat
#
### Jelaskan tag HTML5 yang kamu ketahui
HTML5 merupakan perbaruan terbaru dari HTML, syntax yang digunakan pada HTML5 lebih sederhana dan spesifik dari pendahulunya. Sebagai contoh dahulu harus mendefinisikan <'div> untuk berbagai macam elemen, tapi dengan HTML5 penandaan section dengan syntax lebih sederhana <'nav> untuk membuat navigasi. 

Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1.	Selektor Tag = selector yang memilih elemen berdasarkan nama tag
2.	Selektor Class = selector yang memilih elemen berdasarkan nama class
3.	Selektor ID = selector yang memilih elemen berdasarkan nama class namun digunakan pada satu elemen saja. Selector id ditandai dengan tanda pagar (#)
4.	Selektor Atribut = selector yang memilih elemen berdasarkan atribut
5.	Selektor Universal yaitu selector yang digunakan untuk semua elemen Selector universal ditandai dengan tanda bintang (*)
6.	Psedeu Selector = psedeu selector memiliki 2 macam psedeu selector yaitu psedeu-class selektor untuk memilih state pada elemen. Contohnya seperti elemen saat diklik, saat fokus, saat disentuh, dan lain sebagainya. Dan psedeu-element selector selector untuk memilih state pada elemen tertentu dengan bantuan <'span>
#
### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. download bootstrap lalu extract dan ditempatkan pada folder static
2. lalu salin Link bootstrap pada base.html, salin juga pada halaman login, create-task dan todolist.




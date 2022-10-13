# Tugas 6: Javascript dan AJAX

## Nama : Ikra Bhaktiananda
## NPM  : 2106637580
#

### Link Heroku
https://tugas2pbpikra.herokuapp.com/todolist/login/
#

### 1.	Jelaskan perbedaan antara asynchronous programming dengan synchronous programming

    Asyncrhonous : 
    Asynchrounous program akan bisa menjalankan beberapa multiple task pada waktu yang sama. Ketika sebuah function asyncrhonous dipanggil, baris code selanjutnya bisa dijalankan tanpa perlu menunggu function sebelumnya selesai dijalankan (concurrent).
    
    
    Synchronous
    Synchronous program akan menjalankan task satu-satu secara berurutan. Ketika sebuah task dijalankan, instruksi untuk menjalankan task lainnya akan diblokir. Jadi program synchronous harus menunggu task bersangkutan selesai terlebih dahulu baru bisa menjalankan task selanjutnya berikutnya (sequential).
    

### 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini

Paradigma Event-Driven Programming merupakan  ketika sebuah program dieksekusi berdasarkan event yang terjadi. Paradigma ini sangat bergantung pada event, sehingga alur jalan dari program mampu dijalankan seperti konsep asynchronous programming yang tidak sequential. Salah satu contoh penerapannya pada tugas kali ini adalah ketika button `add` pada `add task` diklik, program akan selalu menjalankan suatu fungsi untuk membuat task baru ketika terdapat event yaitu click `document.getElementById("addtaskbutton").onclick = addTodolistModal` 

### 3. Jelaskan penerapan asynchronous programming pada AJAX.

Pada JavaScript, AJAX akan menerapkan konsep asynchronous programming ketika akan mengeksekusi suatu task pada program. Pada tugas ini, AJAX berpengaruh dalam pengambilan data serta ketika menanggapi suatu response dalam bentuk JSON. Ketika kita menekan tombol add pada program, maka program akan melakukan AJAX POST yang mana akan mengirim data ke server. Kemudian, data akan ditangkap dan dikirimkan ke server tanpa adanya reload pada browser. Kita hanya perlu menambahkan library JQuery pada templates todolist.html, lalu JQuery tersebut akan melakukan pemanggilan function success dan error

### 4. Jelaskan penerapan asynchronous programming pada AJAX.

1. Firstly saya menambahkan beberapa function pada views.py untuk meng-implementasikan fungsi ajax yang mengembalikan data dalam bentuk JSON.
2. Lalu saya melakukan routing pada urls.py untuk menambahkan function yang sudah dibuat.
3. Lalu saya meng-edit todolist.html dan membuat script ajax get untuk mengganti for loop awal saya dengan fungsi GET ajax.
4. Lalu mengubah pemetaan create_task dengan template modal bootstrap
5. Lalu meng-implementasikan fungsi POST pada script ajax untuk menambahkan data dari modal.
6. Lalu fitur create_task menjadi asynchronous




# Travel Insurance Claim Prediction
**Ikhsan Herdi Fajriyanto**

# Introduction

Perusahaan penyedia layanan asuransi perjalanan pihak ketiga yang berkantor pusat di Singapura. Asuransi perjalanan merupakan salah satu jenis asuransi yang memberikan perlindungan selama kita melakukan perjalanan baik di dalam negeri maupun luar negeri. Beberapa negara bahkan telah mewajibkan para pelancong untuk memiliki asuransi perjalanan, misalnya negara-negara di Eropa dan Amerika. Besarnya premi tergantung pada cakupan yang diinginkan, lamanya perjalanan, dan tujuan perjalanan. Perusahaan yang bergerak di bidang asuransi perjalanan ingin mengetahui pemegang polis yang akan mengajukan klaim asuransi untuk mendapatkan cakupan. Data pemegang polis pada perusahaan asuransi merupakan data historis yang terdiri dari destinasi, produk asuransi, dan sebagainya.

# Context

Pada studi kasus ini terdapat perusahaan asuransi yang menawarkan jasa asuransi kepada calon traveler. Berdasarkan dari dataset tersebut banyak orang yang mengajukan klaim untuk asuransi
mereka saat mereka melakukan perjalanan, namun tidak semua klaim dapat di terima. Maka dari itu perusahaan ingin mengetahui informasi siapa saja customer yang berhak menerima klaim
(mengalami resiko yang akan dipertanggung oleh perusahaan) dan mana yang ditolak. Karena dalam hal ini perusahaan juga akan terbantu dalam hal mengurangi beban, kinerja dan waktu serta kualitas pelayanan penyedia asuransi perjalanan kepada para pelaku perjalanan.

**Target:**
`0` : **Klaim ditolak/Tidak Menerima Klaim** 
`1` : **Klaim diterima/Berhak Menerima Klaim**

# Problem Statement

Terdapat `44.328` data dari customer yang ingin mengajukan klaim, banyaknya calon pelaku perjalanan yang mengajukan Claim bisa memakan waktu dan kinerja yang dibutuhkan para agensi penyedia asuransi perjalanan. Oleh karena itu agensi hanya ingin memberikan Claim bagi pelaku perjalanan yang benar-benar mengajukan Claim dan telah mengisi formulir pengajuan secara benar dan lengkap. Selain itu agensi hanya ingin memberikan Claim berdasarkan produk asuransi yang memiliki kemungkinan yang sangat besar untuk di-klaim oleh pelaku perjalanan.

Dari dataset yang diberikan, banyak pelaku perjalanan yang tidak mengisi kolom jenis kelamin dan dianggap mengisi formulir pengajuan asuransi secara tidak lengkap, atau mengisi data yang dianggap tidak sah oleh agensi seperti durasi perjalanan lebih dari 18 bulan (sesuai durasi standar mayoritas asuransi perjalanan), atau mengajukan Claim untuk produk asuransi yang tidak memiliki kemungkinan yang sangat besar untuk di-klaim.

# Goals

Berdasarkan permasalah tersebut, maka perusahaan ingin memprediksi kemungkinan seorang calon pelaku perjalanan untuk berhak menerima Claim, sehingga tidak menyia-nyiakan waktu, beban, dan kinerja perusahaan dalam memberikan Claim asuransi perjalanan namun tidak diterima oleh calon pelaku perjalanan tersebut.

Dan juga, perusahaan ingin mengetahui apa/faktor/variabel apa yang membuat seseorang berhak menerima Claim, sehingga mereka dapat membuat rencana yang lebih baik dan meningkatkan kualitas pelayanan asuransi dan Claim untuk pelaku perjalanan dan bisa membuat pelaku perjalanan puas dalam pelayanan asuransi.

# Analytics Approach

Pada kesempatan ini yang akan dilakukan adalah menganalisis data untuk menemukan pola yang membedakan calon pelaku perjalanan yang berhak menerima Claim dan tidak berhak menerima Claim.
Kemudian akan membangun model klasifikasi yang akan membantu perusahaan untuk dapat memprediksi probabilitas seorang pelaku perjalanan berhak untuk menerima Claim atau tidak.

# Evaluation Matrics
![0_wPxmui5uaThY8_ab](https://github.com/user-attachments/assets/7bb4e387-aae5-4a6f-8e60-95896a33cdb0)
**Type 1 error** : False Positive
Konsekuensi: sia-sianya waktu, beban, dan kinerja perusahaan dalam pelayanan asuransi karena calon pelaku perjalanan tidak menerima Claim, meskipun sudah mengajukannya.

**Type 2 error** : False Negative
Konsekuensi: penurunan kualitas pelayanan asuransi bagi pelaku perjalanan karena calon pelaku perjalanan harus menerima Claim, meskipun tidak mengajukannya.

Berdasarkan konsekuensinya, maka sebisa mungkin yang akan kita lakukan adalah membuat model yang dapat mengurangi beban dan kinerja perusahaan, tetapi tanpa menurunkan kualitas pelayanan asuransi bagi para pelaku perjalanan. Jadi kita ingin sebanyak mungkin prediksi kelas positif yang benar, dengan sesedikit mungkin prediksi false positive.

# Data Undetstanding

- `Agency`: Name of agency.
- `Agency Type`: Type of travel insurance agencies.
- `Distribution Channel`: Channel of travel insurance agencies.
- `Product Name`: Name of the travel insurance products.
- `Gender`: Gender of insured.
- `Duration`: Duration of travel.
- `Destination`: Destination of travel.
- `Net Sales`: Amount of sales of travel insurance policies.
- `Commission (in value)`: Commission received for travel insurance agency.
- `Age`: Age of insured.
- `Claim`: Claim status.

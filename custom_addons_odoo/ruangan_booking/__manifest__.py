# -*- coding: utf-8 -*-
{
    'name': "ruangan_booking",
    'summary': "Modul untuk Pemesanan dan Manajemen Ruangan",
    'description': """
        Modul ini digunakan untuk mengelola pemesanan ruangan, termasuk
        fitur untuk menambah, mengedit, dan melihat informasi tentang ruangan
        serta pemesanan yang dilakukan oleh pengguna.
    """,
    'author': "Nama Anda atau Perusahaan Anda",
    'website': "https://www.yourcompany.com",

    # Kategori dapat digunakan untuk memfilter modul dalam daftar modul
    'category': 'Uncategorized',
    'version': '0.1',

    # Modul yang diperlukan agar modul ini berfungsi dengan baik
    'depends': ['base'],

    # Selalu dimuat
    'data': [
        'security/ir.model.access.csv',  # Pastikan Anda menambahkan file akses keamanan
        'views/views.xml',                 # File tampilan untuk modul
        'views/pemesanan_list.xml',        # Tambahkan file untuk daftar pemesanan
        'views/pemesanan_detail.xml',      # Tambahkan file untuk detail pemesanan
        'views/create_pemesanan.xml',      # Tambahkan file untuk form pembuatan pemesanan
    ],

    # Hanya dimuat dalam mode demonstrasi
    'demo': [
        'demo/demo.xml',                   # File demo untuk modul
    ],
}

# -*- coding: utf-8 -*-
# from odoo import http


# class RuanganBooking(http.Controller):
#     @http.route('/ruangan_booking/ruangan_booking', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ruangan_booking/ruangan_booking/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ruangan_booking.listing', {
#             'root': '/ruangan_booking/ruangan_booking',
#             'objects': http.request.env['ruangan_booking.ruangan_booking'].search([]),
#         })

#     @http.route('/ruangan_booking/ruangan_booking/objects/<model("ruangan_booking.ruangan_booking"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ruangan_booking.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class RuanganBooking(http.Controller):
    
    @http.route('/ruangan_booking/', auth='public', website=True)
    def index(self, **kw):
        return "Selamat datang di sistem pemesanan ruangan!"

    @http.route('/ruangan_booking/pemesanan', auth='public', website=True)
    def list(self, **kw):
        # Mengambil semua pemesanan
        pemesanan_list = request.env['ruangan_booking.pemesanan'].search([])
        return request.render('ruangan_booking.pemesanan_list', {
            'pemesanan_list': pemesanan_list,
        })

    @http.route('/ruangan_booking/pemesanan/<int:pemesanan_id>', auth='public', website=True)
    def object(self, pemesanan_id, **kw):
        # Mencari pemesanan berdasarkan ID
        pemesanan = request.env['ruangan_booking.pemesanan'].browse(pemesanan_id)
        return request.render('ruangan_booking.pemesanan_detail', {
            'pemesanan': pemesanan
        })

    @http.route('/ruangan_booking/create', auth='public', website=True, methods=['GET', 'POST'])
    def create_pemesanan(self, **kw):
        if request.httprequest.method == 'POST':
            # Menerima data dari formulir
            nomor_pemesanan = kw.get('nomor_pemesanan')
            ruangan_id = kw.get('ruangan_id')
            nama_pemesanan = kw.get('nama_pemesanan')
            tanggal_pemesanan = kw.get('tanggal_pemesanan')
            catatan_pemesanan = kw.get('catatan_pemesanan')

            # Membuat pemesanan baru
            request.env['ruangan_booking.pemesanan'].create({
                'nomor_pemesanan': nomor_pemesanan,
                'ruangan_id': ruangan_id,
                'nama_pemesanan': nama_pemesanan,
                'tanggal_pemesanan': tanggal_pemesanan,
                'catatan_pemesanan': catatan_pemesanan,
            })

            return http.local_redirect('/ruangan_booking/pemesanan')

        # Jika metode GET, tampilkan formulir pembuatan pemesanan
        ruangan_list = request.env['ruangan_booking.ruangan'].search([])
        return request.render('ruangan_booking.create_pemesanan', {
            'ruangan_list': ruangan_list,
        })


# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ruangan_booking(models.Model):
#     _name = 'ruangan_booking.ruangan_booking'
#     _description = 'ruangan_booking.ruangan_booking'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions


class MasterRuangan(models.Model):
    _name = 'ruangan_booking.master_ruangan'
    _description = 'Master Ruangan'

    name = fields.Char(string='Nama Ruangan', required=True)
    tipe_ruangan = fields.Selection([
        ('meeting_kecil', 'Meeting Room Kecil'),
        ('meeting_besar', 'Meeting Room Besar'),
        ('aula', 'Aula')
    ], string='Tipe Ruangan', required=True)
    lokasi_ruangan = fields.Selection([
        ('1A', '1A'),
        ('1B', '1B'),
        ('1C', '1C'),
        ('2A', '2A'),
        ('2B', '2B'),
        ('2C', '2C')
    ], string='Lokasi Ruangan', required=True)
    foto_ruangan = fields.Binary(string='Foto Ruangan', required=True)
    kapasitas_ruangan = fields.Integer(string='Kapasitas Ruangan', required=True)
    keterangan = fields.Text(string='Keterangan')


class PemesananRuangan(models.Model):
    _name = 'ruangan_booking.pemesanan_ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True, copy=False, readonly=True,
                                   default=lambda self: self.env['ir.sequence'].next_by_code('ruangan.pemesanan'))
    ruangan_id = fields.Many2one('ruangan_booking.master_ruangan', string='Ruangan', required=True)
    nama_pemesanan = fields.Char(string='Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Date(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('ongoing', 'On Going'),
        ('done', 'Done')
    ], string='Status Pemesanan', default='draft')
    catatan_pemesanan = fields.Text(string='Catatan Pemesanan')

    @api.constrains('tanggal_pemesanan', 'ruangan_id')
    def _check_duplicate_booking(self):
        for record in self:
            overlapping_bookings = self.search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id)
            ])
            if overlapping_bookings:
                raise exceptions.ValidationError("Ruangan sudah dipesan pada tanggal ini.")

    @api.constrains('nama_pemesanan')
    def _check_unique_booking_name(self):
        for record in self:
            existing_booking = self.search([
                ('nama_pemesanan', '=', record.nama_pemesanan),
                ('id', '!=', record.id)
            ])
            if existing_booking:
                raise exceptions.ValidationError("Nama Pemesanan sudah digunakan.")

    def action_confirm(self):
        self.status_pemesanan = 'ongoing'

    def action_done(self):
        self.status_pemesanan = 'done'

from odoo import models, fields, api

class MasterRuangan(models.Model):
    _name = 'master.ruangan'
    _description = 'Master Ruangan'

    name = fields.Char(string="Nama Ruangan", required=True)
    tipe = fields.Selection([('small', 'Meeting Room Kecil'), ('large', 'Meeting Room Besar'), ('aula', 'Aula')], required=True)
    lokasi = fields.Selection([('1A', '1A'), ('1B', '1B'), ('2A', '2A')], required=True)
    foto = fields.Binary(string="Foto Ruangan", required=True)
    kapasitas = fields.Integer(string="Kapasitas Ruangan", required=True)
    keterangan = fields.Text(string="Keterangan")

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string="Nomor Pemesanan", required=True)
    ruangan_id = fields.Many2one('master.ruangan', string="Ruangan", required=True)
    nama_pemesan = fields.Char(string="Nama Pemesan", required=True)
    tanggal_pemesanan = fields.Date(string="Tanggal Pemesanan", required=True)
    status = fields.Selection([('draft', 'Draft'), ('ongoing', 'On Going'), ('done', 'Done')], default='draft')
    catatan_pemesanan = fields.Text(string="Catatan Pemesanan")

    _sql_constraints = [
        ('unique_nomor_pemesanan', 'unique(nomor_pemesanan)', 'Nomor pemesanan harus unik!')
    ]

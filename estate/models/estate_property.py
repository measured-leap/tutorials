import datetime
from odoo import fields, models

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(required=True, string='Name')
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date(copy=False, default=lambda self: fields.Date.to_string(
            datetime.date.today() + datetime.timedelta(days=90)
        ), string='Date Availability')
    expected_price = fields.Float(required=True, string='Expected Price')
    selling_price = fields.Float(copy=False, readonly=True, string='Selling Price')
    bedrooms = fields.Integer(default=2, string='Bedrooms')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection([
        ('north', 'North'),
        ('south', 'South'),
        ('east', 'East'),
        ('west', 'West'),
    ], string='Garden Orientation')


    # sql constraints
    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0 OR id > 25)', 'expected price can\'t be negative.'),
    ]
    active = fields.Boolean(default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled'),
    ], required=True, copy=False, default='new', string='Status')
    
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'license': 'LGPL-3',
    "name" : "Change Custom Color Palette for CE",
    "version" : "11.0",
    "author" : "saas tools",
    'price': 9.90,
    'currency': 'EUR',
    "category" : "Extra Tools",
	"summary": "Change the Odoo color palette made by (W360S)",
    'description': "For Odoo Community Version 11.0, this module replaces the default odoo color & background with a single gray image background. By replacing the image file in this module, you can further personalize the Odoo Apps Switcher page. This is a very simply module. It serves as an ideal example for those who are learning how to build modules with Odoo. or you want to change your own color just go to color_palette/static/src/less/variables.less and do change for whatever color you want to change follow code bellow and change these: @odoo-brand-primary: #0077cd; @odoo-brand-optional: #4d8496; @odoo-brand-secondary: #00ce2c; @odoo-brand-lightsecondary: #e2e2e0; as color you want.",
    'maintainer': "World 360° Services",
    'website': 'http://saastools.xyz',
    'images': ['static/description/banner.png'],
    "depends" : ["base", "web_responsive"],
    "init_xml" : [],
    "demo_xml" : [],
        "data" : [
        'views/color_change.xml',
    ],
    "test" : [
    ],
    "auto_install": False,
    "application": False,
    "installable": True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

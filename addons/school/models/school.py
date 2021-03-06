from odoo import fields, models, api, _
from odoo.exceptions import UserError

class SchoolProfile(models.Model):
    _name = "school.profile"

    name = fields.Char(string="School Name", copy=False, default="Sunny Leone")
    email = fields.Char(string="Email", copy=False)
    phone = fields.Char("Phone", copy=False)
    is_virtual_class = fields.Boolean(string="Virtual Class Support?")
    school_rank = fields.Integer(string="Rank")
    result = fields.Float(string="Result")
    address = fields.Text(string="Address")
    estalish_date = fields.Date(string="Establish Date")
    open_date = fields.Datetime("Open Date")
    school_type = fields.Selection([('public','Public School'),
                                    ('private', 'Private School')],
                                   string="Type of School",
                                   )
    documents = fields.Binary(string="Documents")
    document_name = fields.Char(string="File Name")
    school_image = fields.Image(string="Upload School Image", max_width=100,
                                max_height=100)
    school_description = fields.Html(string="Description", copy=False)
    auto_rank = fields.Integer(compute="_auto_rank_populate", string="Auto "
                                                                     "Rank",
                               store=True, help="This is auto populate data "
                                                "based on school type change.")
    # TEST
    # @api.multi
    # def test_button_box(self):
    #     return {
    #         'name': ('School profiles'),
    #         'domain':[],
    #         'view_type': 'form',
    #         'res_model': 'school.profile',
    #         'view_id': False,
    #         'view_mode': 'tree, form',
    #         'type': 'ir.actions.act_window',
    #     }
    # END-TEST


    _sql_constraints = [
        ('name_unique', 'unique (name)', "Please enter unique school name, Given school name already exists.")
    ]


    @api.depends("school_type")
    def _auto_rank_populate(self):
        for rec in self:
            if rec.school_type == "private":
                rec.auto_rank = 50
            elif rec.school_type == "public":
                rec.auto_rank = 100
            else:
                rec.auto_rank = 0

    @api.model
    def name_create(self, name):
        rtn = self.create({"name":name, "email":"abc@gmail.com"})
        return rtn.name_get()[0]

    def name_get(self):
        student_list = []
        for school in self:
            print(self, school)
            name = school.name
            if school.school_type:
                name += " ({})".format(school.school_type)
            student_list.append((school.id, name))
        return student_list

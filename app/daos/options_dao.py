from sqlalchemy import Column, String, Boolean, BigInteger, desc, func, Date
from app.commons.database import model, BaseModel, DatabaseTemplate
from app.commons.database_mixin import IdMixin, CreatedAtMixin, UpdatedAtMixin

__author__ = 'zhaowenlei'


class Option(IdMixin, BaseModel):

    opt_value = Column(String(20))
    opt_title = Column(String(100), default='')
    opt_type = Column(String(50))
    opt_selected = Column(BigInteger)
    opt_order = Column(BigInteger, default=None)
    sub_opt_type = Column(String(20), default=None)


@model(Option)
class OptionDao(DatabaseTemplate):

    def gets_by_type(self, opt_type):
        return self.session.query(self.model_cls).filter(self.model_cls.opt_type == opt_type).all()

    def get_by_type_value(self, opt_type, opt_value):
        return self.session.query(self.model_cls)\
            .filter(self.model_cls.opt_type == opt_type,self.model_cls.opt_value == opt_value)\
            .first()
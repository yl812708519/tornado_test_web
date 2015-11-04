

from sqlalchemy import Column, BigInteger, String, Integer, Boolean, DateTime, Float
from app.commons.database import BaseModel, DatabaseTemplate, model
from app.commons.database_mixin import {% if has_id %}{% if is_string_id %}IdStringMixin, {%else%}IdMixin, {%end%}{%end%} CreatedAtMixin, UpdatedAtMixin{% if has_is_deleted %}, IsDeletedMixin{%end%}

{% set column_type_map = dict(
varchar='String({})',
bigint='BigInteger',
text='Text',
char='String(0)',
decimal='Float',
int='Integer',
datetime='DateTime',
tinyint='Integer')%}
class {{class_name}}({% if has_id %}{% if is_string_id %}IdStringMixin, {%else%}IdMixin, {%end%}{%end%}{% if has_created_at %}CreatedAtMixin, {%end%}{% if has_updated_at %}UpdatedAtMixin, {%end%}{% if has_is_deleted %}IsDeletedMixin, {%end%}BaseModel):
{% for table_meta in table_metas%}{% if not table_meta.column_name in ['id', 'created_at', 'updated_at', 'deleted_at'] %}
    # {{table_meta.column_comment}}
    {% if table_meta.data_type in ['varchar', 'char', 'text'] %}{{table_meta.column_name}} = Column({{column_type_map[table_meta.data_type].format(table_meta.character_maximum_length)}}{%if table_meta.column_default is not None%}, default='{{table_meta.column_default}}'{% end %}){% elif 'tinyint' == table_meta.data_type and (table_meta.column_name.startswith('is') or table_meta.column_name.startswith('has')) %}{{table_meta.column_name}} = Column(Boolean{%if table_meta.column_default is not None%}{{""", default=False""" if table_meta.column_default == '0' else """, default=True"""}}{%end%}){% else %}{{table_meta.column_name}} = Column({{column_type_map[table_meta.data_type]}}, default={{table_meta.column_default}}){% end %}
{% end%}{% end %}

@model({{class_name}})
class {{class_name}}Dao(DatabaseTemplate):
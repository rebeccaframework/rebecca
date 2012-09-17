from markupsafe import Markup

class Grid(object):
    def __init__(self, columns, table_attrs=None, head_attrs=None, row_attrs=None):
        self.columns = columns
        self.table_attrs = {}
        if table_attrs:
            self.table_attrs = table_attrs
        self.head_attrs = {}
        if head_attrs:
            self.head_attrs = head_attrs
        self.row_attrs = {}
        if row_attrs:
            self.row_attrs = row_attrs


    def __call__(self, items):
        return Markup("".join(self.render(items)))

    def render_table_attrs(self):
        if not self.table_attrs:
            return u""

        return " " + " ".join(['{0}="{1}"'.format(k, v) for k, v in self.table_attrs.items()])

    def render(self, items):
        yield u'<table{0}>'.format(self.render_table_attrs())
        for h in self.render_head():
            yield h

        for item in items:
            for part in self.render_row(item):
                yield part

        yield u'</table>'

    def render_head(self):
        yield u'<tr>'
        for n,_ in self.columns:
            yield u'<th>{0}</th>'.format(n)
        yield u'</tr>'

    def render_row(self, item):
        yield u'<tr>'
        for _,c in self.columns:
            yield u'<td>{}</td>'.format(c(item))
        yield u'</tr>'

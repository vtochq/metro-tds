from controlcenter import Dashboard, widgets
from tds.models import Display

class MyBarChart(widgets.SingleBarChart):
    def values(self):
        return [(1,2),(2,3)]
    def series(self):
        # Y-axis
        return [y for x, y in self.values]

    def labels(self):
        # Duplicates series on x-axis
        return self.series

    def legend(self):
        # Displays labels in legend
        return [x for x, y in self.values]

class ModelItemList(widgets.ItemList):
    model = Display
    queryset = model.objects.all()
    list_display = ('pk', 'field', 'get_foo')
    list_filters = ('pk', 'field', 'get_foo')
    list_display_links = ('field', 'get_foo')
    #template_name = 'my_custom_template.html'

    def get_foo(self, obj):
        return 'foo'
    get_foo.allow_tags = True
    get_foo.short_description = 'Foo!'



class MyDashboard(Dashboard):
    widgets = (
        ModelItemList,
        MyBarChart,
    )
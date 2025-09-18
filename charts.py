import plotly.express as px

class drow_chart():
    def __init__(self,df):
        self.df = df

    def line_chart(self, x, y, title):
        fig = px.line(self.df,
                       x=x,
                       y=y,
                     title=title)
        return fig
    
    def pie_chart(self,names,values,title,color,color_discrete_map):
        fig = px.pie(self.df,
                     names=names,
                     values=values,
                     title=title,
                     color=color,
                     color_discrete_map=color_discrete_map)
        return fig

    def histogram_chart(self,x, y, title,histfunc,color_discrete_sequence,nbins):
        fig = px.histogram (self.df,
                            x=x,
                            y=y,
                            title=title,
                            histfunc=histfunc,
                            color_discrete_sequence = ['indianred'], 
                            nbins=nbins
        )
        return fig

    def Box_cahrt(self,x,y):
        fig = px.box(self.df,
                     x=x,
                     y=y)
        return fig

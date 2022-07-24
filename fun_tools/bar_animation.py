import bar_chart_race as bcr
df = bcr.load_dataset('covid19_tutorial')
bcr.bar_chart_race(
        df=df,
        filename='./images/covid19_horiz.mp4',
        orientation='v',
        sort='desc',
        n_bars=8,
        fixed_order=False,
        fixed_max=True,
        steps_per_period=20,
        period_length=500,
        # end_period_pause=0,
        interpolate_period=False,
        period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'},
        # period_template='%B %d, %Y',
        period_summary_func=lambda v, r: {'x': .98, 'y': .2,
                                          's': f'Total deaths: {v.sum():,.0f}',
                                          'ha': 'right', 'size': 11},
        perpendicular_bar_func='median',
        # colors='dark12',
        title='COVID-19 Deaths by Country',
        bar_size=.95,
        # bar_textposition='inside',
        # bar_texttemplate='{x:,.0f}',
        # bar_label_font=7,
        # tick_label_font=7,
        # tick_template='{x:,.0f}',
        shared_fontdict=None,
        scale='linear',
        fig=None,
        writer=None,
        bar_kwargs={'alpha': .7},
        # fig_kwargs={'figsize': (6, 3.5), 'dpi': 144},
        filter_column_colors=False)
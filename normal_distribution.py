import pandas as pd
import plotly.figure_factory as ff 
f=pd.read_csv("project.csv")
figure=ff.create_distplot([f["Avg Rating"].tolist()],["Ratings of different mobile phone brands"])
figure.show()
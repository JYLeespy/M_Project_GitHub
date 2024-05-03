import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000
import os


class GraphBuilder:
    def __init__(self, filepath, category="", imgshow=True, autosave=False, graph_item = []):
        self.path = os.path.dirname(filepath)
        self.category = category
        self.imgshow = imgshow
        self.autosave = autosave
        self.keydatas=[]
        with open(filepath, 'r') as r:
            self.readline = r.readlines()
        first_line = self.readline[0].rstrip()  # \n 제거
        self.keydatas = first_line.split('\t')  # 리스트로 분할
        self.graph_item = graph_item

        # print(self.keydatas)

    def make_dataframe(self):
        data = {}
        col_index = {}
        new_readline = []
        col_count = 0
        first_line_split = self.readline[0].split('\t')
        for first_line_col in first_line_split:
            if first_line_col in self.graph_item:
                col_index[first_line_col] = col_count
            col_count += 1
        for line in self.readline:
            filtering = False
            for col in col_index:
                if line.split('\t')[col_index[col]] == '-9999.0000':
                    filtering = True
                else:
                    pass
            if filtering:
                continue
            else:
                new_readline.append(line)
        firstline = True
        for line in new_readline:
            if firstline:
                firstline = False
                continue

            # print(f'line : {line}')
            temp_linedata = line.rstrip()
            linedata = temp_linedata.split('\t')

            line_count = 0
            for cols in linedata:

                # 시간 그룹 열 추가
                if line_count == 2:
                    if cols == 'Time':
                        dict_key = 'TimeGroup'
                        dict_value = 'TimeGroup'
                    else:
                        hour_value = int(cols.split(":")[0])
                        h0 = 4
                        h1 = 8
                        h2 = 12
                        h3 = 16
                        h4 = 20
                        if hour_value <= h0:
                            time_group = '01~04'
                        elif hour_value > h0 and hour_value <= h1:
                            time_group = '05~08'
                        elif hour_value > h1 and hour_value <= h2:
                            time_group = '09~12'
                        elif hour_value > h2 and hour_value <= h3:
                            time_group = '13~16'
                        elif hour_value > h3 and hour_value <= h4:
                            time_group = '17~20'
                        else:
                            time_group = '21~24'
                        dict_key = 'TimeGroup'
                        dict_value = time_group
                    try:
                        temp_data = data[dict_key]
                    except:
                        data[dict_key] = []
                        temp_data = data[dict_key]
                    temp_data.append(dict_value)
                    data[dict_key] = temp_data

                # 데이터 열 추가
                dict_key = self.keydatas[line_count]
                dict_value = cols
                try:
                    temp_data = data[dict_key]
                except:
                    data[dict_key] = []
                    temp_data = data[dict_key]

                if line_count >= 10:
                    temp_data.append(float(dict_value))
                else:
                    temp_data.append(dict_value)
                data[dict_key] = temp_data
                line_count += 1

        self.df = pd.DataFrame(data)
        # print(f'len :{len(self.df)}')
    def boxflot(self, cols, size=(10,6), x_label="", y_label=""):
        # Box Flot 그릴 항목이 2개인 경우 선정
        boxflot_qty = len(cols)
        groups = []
        labels = []
        for column in cols:
            groups.append(self.df[column])
            labels.append(column)
        if boxflot_qty == 1:
            grouped_df = self.df.groupby('TimeGroup').agg({cols[0]: 'mean'}).reset_index()
            title = cols[0]
        else:  # boxflot_qty == 2:
            grouped_df = self.df.groupby('TimeGroup').agg({cols[0]: 'mean', cols[1]: 'mean'}).reset_index()
            title = f'{cols[0]}_{cols[1]}'
        fig = plt.figure(figsize=size)
        fig.set_facecolor('white')
        # fig.title(title)

        ax = fig.add_subplot()
        # Data Index Label Settings
        xticks = range(len(grouped_df))
        # ax.plot(xticks, grouped_df[self.ui.label_item1.text()], color='r', marker='o')  ## 평균 선 그래프
        # ax.plot(xticks, grouped_df[self.ui.label_item2.text()], color='k', marker='o')  ## 평균 선 그래프
        xunit = xticks[1] - xticks[0]  ## 눈금 단위
        for xtick in xticks:  ## 각 눈금에 대하여 박스 플롯 두개씩 그린다.
            date = grouped_df.iloc[xtick]['TimeGroup']
            target_df = self.df[self.df['TimeGroup'] == date]
            if boxflot_qty == 1:
                list_of_df = [target_df[cols[0]]]
            else: # boxflot_qty == 2:
                list_of_df = [target_df[cols[0]], target_df[cols[1]]]
            self.draw_boxflot(list_of_df, xtick, xunit, ax, colors=['r', 'k'], facecolors=['y', 'b'],padding=0.8, width=0.3)
        # Axis Label Settings
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        tick_step = 1
        ax.set_xticks(xticks[::tick_step])
        ax.set_xticklabels(grouped_df['TimeGroup'].to_list()[::tick_step])
        if self.imgshow:
            plt.show()
        if self.autosave:
            self.save(title)

    def boxflot_AVI(self, cols, nominal, usl, lsl, datatype, unit, spec_styles, checkopt):
        # Box Flot 그릴 항목이 2개인 경우 선정
        size = (10, 6)
        boxflot_qty = len(cols)
        groups = []
        labels = []

        for column in cols:
            try:
                groups.append(self.df[column])
                labels.append(column)
            except KeyError:
                return False
        if boxflot_qty == 1:
            grouped_df = self.df.groupby('TimeGroup').agg({cols[0]: 'mean'}).reset_index()
            title = cols[0]
        else:  # boxflot_qty == 2:
            grouped_df = self.df.groupby('TimeGroup').agg({cols[0]: 'mean', cols[1]: 'mean'}).reset_index()
            title = f'{cols[0]}  {cols[1]}'

        fig = plt.figure(figsize=size)
        fig.set_facecolor('white')
        ax = fig.add_subplot()
        ax.set_xlabel("Time Group")
        ax.set_ylabel(f'{datatype} ({unit})')

        # Data Index Label Settings
        print(grouped_df)
        xticks = range(len(grouped_df))

        nom_data = []
        usl_data = []
        lsl_data = []
        for x in xticks:
            nom_data.append(nominal)
            usl_data.append(usl)
            lsl_data.append(lsl)

        datas = [nom_data, usl_data, lsl_data]
        item_list = ['label','linewidth','color','linestyle','marker']
        count = 0
        for spec_style in spec_styles:
            data = datas[count]
            ax.plot(xticks, data, label=spec_style[item_list[0]], linewidth=spec_style[item_list[1]], color=spec_style[item_list[2]], linestyle=spec_style[item_list[3]], marker=spec_style[item_list[4]])
            count += 1
        # ax.plot(xticks, grouped_df[self.ui.label_item2.text()], color='k', marker='o')  ## 평균 선 그래프
        try:
            xunit = xticks[1] - xticks[0]  ## 눈금 단위
        except:
            xunit = 1
        for xtick in xticks:  ## 각 눈금에 대하여 박스 플롯 두개씩 그린다.
            date = grouped_df.iloc[xtick]['TimeGroup']
            target_df = self.df[self.df['TimeGroup'] == date]
            # print(f'len(date) : {len(date)}    len(target_df) : {len(target_df)}        len(target_df[0]) : {len(target_df[cols[0]])}')
            if boxflot_qty == 1:
                list_of_df = [target_df[cols[0]]]
            else: # boxflot_qty == 2:
                list_of_df = [target_df[cols[0]], target_df[cols[1]]]
            # print(target_df[cols[0]], target_df[cols[1]])
            self.draw_boxflot(list_of_df, xtick, xunit, ax, colors=['k', 'k'], facecolors=['g', 'b'],padding=0.8, width=0.3)
        # Axis Label Settings
        tick_step = 1
        ax.set_xticks(xticks[::tick_step])
        ax.set_xticklabels(grouped_df['TimeGroup'].to_list()[::tick_step])
        plt.title(title)
        if checkopt[0]:
            plt.show()
        if checkopt[1]:
            plt.savefig(f'{self.path}/{title}.png')

        return True
    def draw_boxflot(self, datas, xtick, xunit, ax, colors, facecolors, width=0.5, zorder=-100, alpha=0.5, padding=0):
        width_offset = (1 - padding) * 0.5
        left_end = xtick - (width_offset * xunit)
        right_end = xtick + (width_offset * xunit)
        position = [left_end, right_end]

        count = 0
        for d in datas:
            self.trend_boxplot(d, position[count], ax, colors[count], facecolors[count], width=width, zorder=zorder,alpha=alpha)
            count += 1
    def trend_boxplot(self, target_data, xtick, ax, color, facecolor, width=0.5, zorder=-100, alpha=0.5):
        # boxplot = ax.violinplot([target_data], positions=[xtick], widths=width)
        # print(f'xtick : >> {xtick}')
        boxplot = ax.boxplot([target_data], positions=[xtick], widths=width, patch_artist=True, zorder=zorder)
        # 박스, 아웃라이어, 중앙선 스타일
        for item in ['boxes', 'fliers', 'medians']:
            for v in boxplot[item]:
                if item == 'boxes':
                    plt.setp(v, facecolor=facecolor, edgecolor=color, alpha=alpha)
                elif item == 'fliers':
                    plt.setp(v, markerfacecolor=color, markersize=2.5, markeredgecolor='none', alpha=alpha)
                else:
                    plt.setp(v, color='white')  ## 나머지 선분 스타일
        for item in ['whiskers', 'caps']:
            for v in zip(boxplot[item][::2], boxplot[item][1::2]):
                if item == 'whiskers':
                    plt.setp(v, color=color, linewidth=1, linestyle='--', alpha=alpha)
                else:
                    plt.setp(v, color=color, linewidth=1, alpha=alpha)
    def save(self, f_name):
        plt.imsave(f'{self.path}/{self.category}/{f_name}')


# filepath = f'D:/ProgramData/Project/M_Project/AVI_Data/DayLotResult_PC2.txt'
# g = GraphBuilder(filepath)
# g.avi_graph_make_dataframe()

# g.boxflot(['FAI_17(deg)'])
# g.boxflot(['FAI_18(deg)'])
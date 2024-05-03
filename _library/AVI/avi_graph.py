import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import datetime

import os
from pathlib import Path
from PIL import Image
import PIL
PIL.Image.MAX_IMAGE_PIXELS = 933120000

class AVI_Graph:
    def add_list(self):
        selected_items = self.ui.list_read.selectedItems()
        select = selected_items[0].text()
        item1 = self.ui.label_item1.text()
        item2 = self.ui.label_item2.text()
        if select == item1 or select == item2:
            pass
        else:
            if item1 == "":
                self.ui.label_item1.setText(select)
            elif item1 != "" and item2 == "":
                self.ui.label_item2.setText(select)
            elif item1 != "" and item2 != "":
                self.ui.label_item1.setText(select)
                self.ui.label_item2.setText("")
    def reset_list(self):
        self.ui.label_item1.setText("")
        self.ui.label_item2.setText("")
    def readfile(self):
        filepath = self.ui.line_path.text()
        with open(filepath, 'r') as r:
            self.readline = r.readlines()
        first_line = self.readline[0].rstrip()  # \n 제거
        self.keydatas = first_line.split('\t')  # 리스트로 분할
        for keys in self.keydatas:
            self.ui.list_read.addItem(keys)
            self.ui.list_read.scrollToBottom()

    def make_dataframe(self):
        data = {}
        firstline = True
        for line in self.readline:
            if firstline:
                firstline = False
                continue
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

    def trend_boxplot(self, target_data, xtick, ax, color, facecolor, width=0.5, zorder=-100, alpha=0.5):
        # boxplot = ax.violinplot([target_data], positions=[xtick], widths=width)
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

    def two_trend_boxplot(self, datas, xtick, xunit, ax, colors, facecolors, width=0.5, zorder=-100, alpha=0.5, padding=0):
        width_offset = (1 - padding) * 0.5
        left_end = xtick - (width_offset * xunit)
        right_end = xtick + (width_offset * xunit)
        position = [left_end, right_end]
        count = 0
        for d in datas:
            self.trend_boxplot(d, position[count], ax, colors[count], facecolors[count], width=width, zorder=zorder, alpha=alpha)
            count += 1

    def run(self):
        self.make_dataframe()
        ## 날짜로 그룹화하여 VALUE 집계
        if self.ui.label_item2.text() == "":
            grouped_df = self.df.groupby('TimeGroup').agg({self.ui.label_item1.text(): 'mean'}).reset_index()
            title = f'{self.ui.label_item1.text()}'
        else:
            grouped_df = self.df.groupby('TimeGroup').agg({self.ui.label_item1.text(): 'mean', self.ui.label_item2.text(): 'mean'}).reset_index()
            title = f'{self.ui.label_item1.text()}, {self.ui.label_item2.text()}'

        fig = plt.figure(figsize=(15, 6))
        plt.title(title)
        fig.set_facecolor('white')
        ax = fig.add_subplot()
        xticks = range(len(grouped_df))  # x축 눈금
        # ax.plot(xticks, grouped_df[self.ui.label_item1.text()], color='r', marker='o')  ## 평균 선 그래프
        # if self.ui.label_item2.text() != "":
        #     ax.plot(xticks, grouped_df[self.ui.label_item2.text()], color='k', marker='o')  ## 평균 선 그래프
        xunit = xticks[1] - xticks[0]  ## 눈금 단위

        for xtick in xticks:  ## 각 눈금에 대하여 박스 플롯 두개씩 그린다.
            date = grouped_df.iloc[xtick]['TimeGroup']
            target_df = self.df[self.df['TimeGroup'] == date]
            if self.ui.label_item2.text() == "":
                list_of_df = [target_df[self.ui.label_item1.text()]]
            else:
                list_of_df = [target_df[self.ui.label_item1.text()], target_df[self.ui.label_item2.text()]]

            self.two_trend_boxplot(list_of_df, xtick, xunit, ax, colors=['r', 'k'],facecolors=['y', 'b'], padding=0.6, width=0.3)

        tick_step = 1  ## 눈금 표시 간격

        ax.set_xlabel(self.ui.line_xtitle.text())
        ax.set_ylabel(self.ui.line_ytitle.text())
        ax.set_xticks(xticks[::tick_step])
        ax.set_xticklabels(grouped_df['TimeGroup'].to_list()[::tick_step])
        plt.show()



        # ax = fig.add_subplot()
        # xticks = range(len(grouped_df))  # x축 눈금
        # ax.plot(xticks, grouped_df['FAI_17(deg)'], color='r', marker='o')  ## 평균 선 그래프
        # ax.plot(xticks, grouped_df['FAI_18(deg)'], color='k', marker='o')  ## 평균 선 그래프
        # xunit = xticks[1] - xticks[0]  ## 눈금 단위
        # for xtick in xticks:  ## 각 눈금에 대하여 박스 플롯 두개씩 그린다.
        #     date = grouped_df.iloc[xtick]['TimeGroup']
        #     target_df = df[df['TimeGroup'] == date]
        #     two_trend_boxplot([target_df['FAI_17(deg)'], target_df['FAI_18(deg)']], xtick, xunit, ax, colors=['r', 'k'],
        #                       facecolors=['y', 'b'], padding=0.6, width=0.3)
        # tick_step = 1  ## 눈금 표시 간격
        #
        # ax.set_xlabel('Time Group')
        # ax.set_ylabel('Value')
        # ax.set_xticks(xticks[::tick_step])
        # ax.set_xticklabels(grouped_df['TimeGroup'].to_list()[::tick_step])
        # plt.show()

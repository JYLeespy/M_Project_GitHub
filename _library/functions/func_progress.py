import sys
class Progressbar:
    def __init__(self):
        self.decimals = 1
        self.barLength = 25
    def run2(self, prefix, count, total, message):
        count = count + 1
        formatStr = "{0:." + str(self.decimals) + "f}"
        percent = formatStr.format(100 * (count / float(total)))
        filledLength = int(round(self.barLength * count / float(total)))
        bar = '■' * filledLength + '□' * (self.barLength - filledLength)
        # sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%', suffix)),
        sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percent, '%  ',message))
        if count >= total:
            sys.stdout.write('\n')
        sys.stdout.flush()

    def run(self, prefix, count, total, message):
        formatStr = "{0:." + str(self.decimals) + "f}"
        percent = formatStr.format(100 * (count / float(total)))
        filledLength = int(round(self.barLength * count / float(total)))
        bar = '■' * filledLength + '□' * (self.barLength - filledLength)
        print('\r', end="")
        print(f'{prefix} |{bar}| {percent}%  {message}', end="")


# import time
# p = Progressbar()
# for i in range(1, 100):
#     p.run3("다운로드",i, 100,"mmmmmmmmmmmmm")
#     time.sleep(0.01)

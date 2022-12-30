import rumps
from datetime import datetime

# Made by Willy Brandes

# a full moon occurred on 2021 July 23rd 10:37 PM EST or July 24th 3:37 AM / UTC
# mean synodic month is 29 days 12 hours 44 minutes 3 seconds or 2551443 total seconds, 1/4 of that is ~637860 seconds
# one day is 86400 seconds, half that is 43200

# 0 - 43200 is Full Moon (+43200)
# 43201 - 594659 is Waning Gibbous (+551459)
# 594660 - 681060 is Last Quarter (~+86400)
# 681061 - 1232519 is Waning Crescent (~+551459)
# 1232520 - 1318920 is New Moon (~+86400)
# 1318921 - 1870379 is Waxing Crescent (~+551459)
# 1870380 - 1956780 is First Quarter (~+86400)
# 1956781 - 2508242 is Waxing Gibbous (~+551459)
# 2508243 - 2551443 is Full Moon (~+86400)

class MoonWatch(object):
    def __init__(self):
        self.app = rumps.App("MoonWatch", "🌝")
        self.app.menu["moon_phase"] = rumps.MenuItem(title="Moon is Happy", callback=None)
        self.phases = [("🌕", "Full Moon"), ("🌖", "Waning Gibbous"), ("🌗", "Last Quarter"), ("🌘", "Waning Crescent"),  ("🌑", "New Moon"), ("🌒", "Waxing Crescent"), ("🌓", "First Quarter"), ("🌔", "Waxing Gibbous")]
        self.full_moon_reference = datetime(2021, 7, 24, 3, 37)
        self.timer = rumps.Timer(self.check_moon, 14400)

    def check_moon(self, sender):
        current_date = datetime.utcnow()

        time_dif = round((current_date - self.full_moon_reference).total_seconds())

        seconds_through_cycle = time_dif % 2551443

        phase_milestones = [43200, 551459, 86400, 551459, 86400, 551459, 86400, 551459, 43200]
        current_count = 0
        i = 0
        while current_count < seconds_through_cycle:
            current_count += phase_milestones[i]

            if i == 8:
                self.update_phase(0)
                break

            if seconds_through_cycle <= current_count:
                self.update_phase(i)

            i += 1

    def update_phase(self, phase_index):
        phase = self.phases[phase_index]
        self.app.title = phase[0]
        self.app.menu.get("moon_phase").title = phase[1]


    def run(self):
        self.timer.start()
        self.app.run()

if __name__ == "__main__":
    moon = MoonWatch()
    moon.run()

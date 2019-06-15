from bs4 import BeautifulSoup
import requests
import argparse
import os

parser = argparse.ArgumentParser(
    description="Script to download abstract from MeiCogSci conference"
)
parser.add_argument(
    "-y", "--year", help="Only download from year specified (default all)"
)
parser.add_argument(
    "-f", "--folder", help="Name of folder to save downloaded abstracts"
)
args = parser.parse_args()


class MeiCogSciAbstractDownloader:
    def __init__(self, args):
        self.args = args
        if not self.args.year:
            self.args.year = []
        else:
            self.args.year = [self.args.year]
        if not self.args.folder:
            self.args.folder = ""
        self.main_link = "https://www.univie.ac.at/meicogsci/php/ocs/index.php/meicog/index/schedConfs/archive"

        all_conferences = self.get_all_conferences_on_page(self.main_link)
        for conference in all_conferences:
            year = self.get_year(conference)
            if not self.args.year or year in self.args.year:
                presentations = self.get_presentations_from_conference(conference, year)
                self.write_presentations_to_file(self.args.folder, presentations)

    def get_all_conferences_on_page(self, main_link):
        conference_lists = requests.get(main_link)
        conference_lists = BeautifulSoup(conference_lists.text, "lxml")
        list_of_all_conferences = conference_lists.find_all("h4")
        return [
            str(conference.find_all("a")[0]).split('"')[1]
            for conference in list_of_all_conferences
        ]

    def get_year(self, conference_link):
        return conference_link.split("/")[-1][-4:]

    def get_presentations_from_conference(self, conference_link, year):
        conference_link = conference_link + "/schedConf/presentations"
        presentations_list = requests.get(conference_link)
        presentations_list = BeautifulSoup(presentations_list.text).find_all("a")
        presentations_list = [
            str(presentation).split('"')[1] for presentation in presentations_list
        ]
        presentations_list = [
            presentation
            for presentation in presentations_list
            if "/paper/" in presentation
        ]
        all_presentations = []
        for presentation in presentations_list:
            number = str(presentation).split("/")[-1]
            presentation = requests.get(presentation)
            presentation = BeautifulSoup(presentation.text).find_all(
                "div", id="content"
            )
            presentation = presentation[0]
            title = presentation.find_all("div", id="title")[0].text
            text = presentation.find_all("div", id="abstract")[0].text
            all_presentations.append([year, number, title, text])
        return all_presentations

    def write_presentations_to_file(self, folder, presentations):
        for year, number, title, text in presentations:
            with open(
                os.path.join(folder, "meicogsci_" + year + "_" + number + ".txt"), "w"
            ) as f:
                f.write("... title: " + title)
                f.write("\n\n\n")
                f.write(text)


if __name__ == "__main__":
    MeiCogSciAbstractDownloader(args)

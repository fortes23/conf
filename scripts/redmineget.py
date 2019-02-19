#!/usr/bin/env python3

"""
Download all attachment from a Redmine ticket/issue in a known folder and 
convert Word documents to PDF.
"""

# Prerequisites: lxml and pyrequests
from lxml import html
import requests
import argparse
import os

from pyutils.utils import style

REDMINE_URL = os.getenv("REDMINE_SERVER", "https://redmineserver")


def getURLdocx(treeHTML):
    """
    Parse HTML and find all the attachments of the ticket/issue.
    """
    attachments = treeHTML.xpath(
        './/div[@class="attachments"]/p/a[@class="icon icon-attachment"]/@href')
    return attachments


def docx2pdf(attachments):
    """
    Download attachments and convert Word documents to pdf.
    """
    for a in attachments:
        aux = a.split('/')
        filename = aux[-1]
        os.system("wget -nc --no-check-certificate {}/{}".format(REDMINE_URL, a))
        if ('.docx' in a or '.doc' in a):
            os.system("lowriter --convert-to pdf {}".format(filename))
            os.system("rm {}".format(filename))


def parser_args():
    parser = argparse.ArgumentParser()
    required = parser.add_argument_group("Required arguments")
    required.add_argument(
        '-t', '--ticket', help='Ticket/Issue number', action='store')
    required.add_argument(
        '-p', '--path', help='Path to save documents', action='store')
    args = parser.parse_args()
    return args


def main():
    args = parser_args()
    if (not args.ticket or not args.path):
        print(style('error', 'Ticket and path must be specified'))
        return
    os.chdir('{}'.format(args.path))
    if (not os.path.isdir(args.ticket)):
        os.mkdir(args.ticket)
    os.chdir('{}/{}'.format(args.path, args.ticket))
    page = requests.get(
        '{}/redmine/issues/{}'.format(REDMINE_URL, args.ticket), verify=False)
    tree = html.fromstring(page.content)
    docx_attach = getURLdocx(tree)
    docx2pdf(docx_attach)


if __name__ == "__main__":
    main()

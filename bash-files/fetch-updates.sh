#!/bin/sh
cp insight_scraper_slack_github_working_dir/csvs/* datapoint_saves/outer_csvs/

cp insight_scraper_slack_github_working_dir/html_saves/* datapoint_saves/outer_html_saves/

rm -rf insight_scraper_slack_github_working_dir

git clone https://github.com/DanielSchussmann/insight_scraper_slack_github_working_dir.git

chmod 777 insight_scraper_slack_github_working_dir

cp internal_secrets.py insight_scraper_slack_github_working_dir/

cp run-nohup.sh insight_scraper_slack_github_working_dir/

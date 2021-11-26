# Data

I began exploring the real estate market in November 2021 using Zillow data. I stopped to reconsider
after learning about the company's shortcomings as an iBuyer and the 
[discontinuation of Zillow Offers](https://www.cnbc.com/2021/11/02/zillow-shares-plunge-after-announcing-it-will-close-home-buying-business.html)
. The main shortcoming was that the majority of Zillow's inventory had depreciated. This put the Zestimate
under a lot of scrutiny.

After some researched, I learned that the most accurate and up to date US real estate data comes from the
[National Association of Realtors (NARs)](https://www.nar.realtor) and their 
[Multiple Listing Service (MLS)](https://www.nar.realtor/competition-in-real-estate) database. Please see the appendix 
Unfortunately, I cannot access that database unless I was a licensed realtor - which I'm not. But
according to Investopedia, Realter.com is "affiliated with the NAR and linked to over 580 regional
Multiple Listing services" ([June 30, 2021](https://www.investopedia.com/best-real-estate-websites-5069964)).
So that's where this project's data comes from - [Realtor.com](https://www.realtor.com/research/data/).

## 1) Folder & File Breakdown

### 1.1) Original

Folders are broken down by **Version**. Each version is different merely in terms of date of creation. For example, 
Version 01 is data that was downloaded from Realtor.com on Thu Nov 25th, 2021.

Each version will contain two folders, one for **inventory** and the other for **market hotness**. Each inventory folder
is composed of two folders, one for **historical** data, and another for **current monthly** data which depends on the 
version of the parent folder.

More details about the original data can be found on the [Realter.com data page](https://www.realtor.com/research/data/)

### 1.2) Modified

>*WIP*

## 2) Data Dictionary
> <sub><sup> Copied from the [Realter.com data page](https://www.realtor.com/research/data/). </sup></sub>

### 2.1) Inventory

| Variable | Definition|
|:---------|:----------|
|Median Listing Price | The median listing price within the specified geography during the specified month.
|Median Listing Price M/M | The percentage change in the median listing price from the previous month.
|Median Listing Price Y/Y | The percentage change in the median listing price from the same month in the previous year.
|Active Listing Count | The count of active listings within the specified geography during the specified month.The active listing count tracks the number of for sale properties on the market, excluding pending listings where a pending status is available. This is a snapshot measure of how many active listings can be expected on any given day of the specified month.
|Active Listing Count M/M | The percentage change in the active listing count from the previous month.
|Active Listing Count Y/Y | The percentage change in the active listing count from the same month in the previous year.
|Days on Market | The median number of days property listings spend on the market within the specified geography during the specified month. Time spent on the market is defined as the time between the initial listing of a property and either its closing date or the date it is taken off the market.
|Days on Market M/M | The percentage change in the median days on market from the previous month.
|Days on Market Y/Y | The percentage change in the median days on market from the same month in the previous year.
|New Listing Count | The count of new listings added to the market within the specified geography. The new listing count represents a typical week’s worth of new listings in a given month. The new listing count can be multiplied by the number of weeks in a month to produce a monthly new listing count.
|New Listing Count M/M | The percentage change in the new listing count from the previous month.
|New Listing Count Y/Y | The percentage change in the new listing count from the same month in the previous year.
|Price Increase Count | The count of listings which have had their price increased within the specified geography. The price increase count represents a typical week’s worth of listings which have had their price increased in a given month. The price increase count can be multiplied by the number of weeks in a month to produce a monthly price increase count.
|Price Increase Count M/M | The percentage change in the price increase count from the previous month.
|Price Increase Count Y/Y | The percentage change in the price increase count from the same month in the previous year.
|Price Decrease Count | The count of listings which have had their price reduced within the specified geography. The price decrease count represents a typical week’s worth of listings which have had their price reduced in a given month. The price decrease count can be multiplied by the number of weeks in a month to produce a monthly price decrease count.
|Price Decrease Count M/M | The percentage change in the price decrease count from the previous month.
|Price Decrease Count Y/Y | The percentage change in the price decrease count from the same month in the previous year.
|Pending Listing Count | The count of pending listings within the specified geography during the specified month, if a pending definition is available for that geography. This is a snapshot measure of how many pending listings can be expected on any given day of the specified month.
|Pending Listing Count M/M | The percentage change in the pending listing count from the previous month.
|Pending Listing Count Y/Y | The percentage change in the pending listing count from the same month in the previous year.
|Median List Price Per Sqft | The median listing price per square foot within the specified geography during the specified month.
|Median List Price Per Sqft M/M | The percentage change in the median listing price per square foot from the previous month.
|Median List Price Per Sqft Y/Y | The percentage change in the median listing price per square foot from the same month in the previous year.
|Median Listing Sqft | The median listing square feet within the specified geography during the specified month.
|Median Listing Sqft M/M | The percentage change in the median listing square feet from the previous month.
|Median Listing Sqft Y/Y | The percentage change in the median listing square feet from the same month in the previous year.
|Avg Listing Price | The average listing price within the specified geography during the specified month.
|Avg Listing Price M/M | The percentage change in the average listing price from the previous month.
|Avg Listing Price Y/Y | The percentage change in the average listing price from the same month in the previous year.
|Total Listing Count | The total of both active listings and pending listings within the specified geography during the specified month. This is a snapshot measure of how many total listings can be expected on any given day of the specified month.
|Total Listing Count M/M | The percentage change in the total listing count from the previous month.
|Total Listing Count Y/Y | The percentage change in the total listing count from the same month in the previous year.
|Pending Ratio | The ratio of the pending listing count to the active listing count within the specified geography during the specified month.
|Pending Ratio M/M | The change in the pending ratio from the previous month.
|Pending Ratio Y/Y | The change in the pending ratio from the same month in the previous year.
 

### 2.2) Hotness

| Variable | Definition|
|:---------|:----------|
|Nielsen HH Rank | The specified zip code, county, or metro area’s rank by household count compared to other zip codes, counties and metro areas. A rank value of 1 is the highest by household count.
|Hotness Rank Within County | In the case of a zip code, this metric represents the zip code’s Hotness rank, by Hotness score, compared to all other zip codes within its county. A rank value of 1 is considered the hottest (highest Hotness score).
|Hotness Rank Within CBSA | In the case of a zip code or county, this metric represents the zip code or county’s Hotness rank, by Hotness score, compared to all other zip codes or counties within its metro area. A rank value of 1 is considered the hottest (highest Hotness score).
|Hotness Rank | The specified zip code, county, or metro area’s Hotness rank, by Hotness score, compared to all other zip codes, counties and metro areas. A rank value of 1 is considered the hottest (highest Hotness score).
|Hotness Rank (Prev) | The specified zip code, county, or metro area’s Hotness rank in the previous month.
|Hotness Rank (Change) | The change in Hotness rank from the previous month. A positive value indicates that the geography’s Hotness has decreased (moved down in ranking), and a negative value indicates that its Hotness has increased (moved up in ranking).
|Hotness Score | The Hotness score is an equally-weighted composite metric of a geography’s supply score and demand score.
|Supply Score | The supply score is an index representing a zip code, county or metro’s median days on market ranking compared to other zip codes, counties, or metros.
|Demand Score | The supply score is an index representing a zip code, county or metro’s listing page views per property ranking compared to other zip codes, counties, or metros.
|Median DOM | The median number of days property listings spend on the market within the specified geography during the specified month. Time spent on the market is defined as the time between the initial listing of a property and either its closing date or the date it is taken off the market.
|Median DOM M/M | The change in days in the median days on market from the previous month.
|Median DOM M/M Perc | The percentage change in the median days on market from the previous month.
|Median DOM Y/Y | The change in days in the median days on market from the same month in the previous year.
|Median DOM Y/Y Perc | The percentage change in the median days on market from the same month in the previous year.
|Median DOM (vs US) | The median days on market in the specified geography divided by the median days on market for the US overall during the same month.
|LDP Unique Viewers Per Property M/M | The change in unique viewers a typical property receives in the specified geography from the previous month.
|LDP Unique Viewers Per Property Y/Y | The change in unique viewers a typical property receives in the specified geography from the same month in the previous year.
|LDP Unique Viewers Per Property  (vs US) | The count of viewers a typical property receives in the specified geography divided by the count of views a typical property receives in the US overall during the same month.
|Median Listing Price | The median listing price within the specified geography during the specified month.
|Median Listing Price M/M | The percentage change in the median listing price from the previous month.
|Median Listing Price Y/Y | The percentage change in the median listing price from the same month in the previous year.
|Median Listing Price  (vs US) | The median listing price within the specified geography divided by the median listing price for the US overall during the same month.
|Quality Flag | Triggered (“1”) when data values are outside of their typical range. While rare, these figures should be reviewed before reporting.

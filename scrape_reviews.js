import gplay from "google-play-scraper";
import fs from 'fs';
import { parse } from 'json2csv';

// Function to fetch reviews for a given app ID
async function fetchReviews(appId, options) {
    try {
        const reviewsData = await gplay.reviews({
            appId: appId,
            ...options
        });
        // console.log(reviewsData)
        return reviewsData;
    } catch (error) {
        console.error('Error fetching reviews:', error);
        return [];
    }
}

// Function to export reviews to a CSV file
async function exportToCSV(reviewsData) {
    try {
        // Extracting keys dynamically from the first review
        const keys = Object.keys(reviewsData.results.data[0]);

        // Preparing fields for json2csv
        const fields = keys.map(key => ({ label: key, value: row => row[key] }));

        // Converting reviews data to CSV format
        const csv = parse(reviewsData.results.data, { fields });

        // Writing CSV data to a file
        fs.writeFileSync('./data/api_reviews.csv', csv, 'utf-8');
        console.log('Reviews exported to api_reviews.csv');
    } catch (error) {
        console.error('Error exporting to CSV:', error);
    }
}

// Main function
async function main() {
    const appId = 'sg.com.gxs.app'; // Change this to the desired app ID
    const options = {
        sort: gplay.sort.RATING,
        num: 500 // Change this value according to the number of reviews you want
    };

    const reviewsData = await fetchReviews(appId, options);
    console.log(reviewsData)
    fs.writeFileSync('./data/api_reviews.json', JSON.stringify(reviewsData), 'utf-8');
}

// Run the main function
main();

const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 3001;
const PUBLIC_DIR = __dirname;

// Request logging middleware
app.use((req, res, next) => {
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
    next();
});

// Helper to check if file exists
const fileExists = (filePath) => {
    try {
        return fs.statSync(filePath).isFile();
    } catch (e) {
        return false;
    }
};

// Custom middleware to handle clean page URLs
app.use((req, res, next) => {
    let reqPath = req.path;

    // Serve root index.html if it exists, otherwise redirect to /en/
    if (reqPath === '/' || reqPath === '') {
        const rootIndexHtml = path.join(PUBLIC_DIR, 'index.html');
        if (fileExists(rootIndexHtml)) {
            return res.sendFile(rootIndexHtml);
        }
        return res.redirect(301, '/en/');
    }

    // Solve for asset files (they have extensions and aren't HTML requests usually)
    const ext = path.extname(reqPath);
    if (ext && ext !== '.html') {
        return next(); // pass to static handler
    }

    // Build the potential file path on disk
    // 1. If path ends with / (e.g. /en/ or /en/destinations/egypt/)
    if (reqPath.endsWith('/')) {
        const indexHtmlPath = path.join(PUBLIC_DIR, reqPath, 'index.html');
        if (fileExists(indexHtmlPath)) {
            return res.sendFile(indexHtmlPath);
        }
    } else {
        // 2. E.g. /en/about-us (no trailing slash, no extension)
        const htmlFilePath = path.join(PUBLIC_DIR, `${reqPath}.html`);
        if (fileExists(htmlFilePath)) {
            return res.sendFile(htmlFilePath);
        }

        // 3. E.g. /en/destinations/egypt (no trailing slash, but index.html exists in subdirectory)
        const dirIndexHtmlPath = path.join(PUBLIC_DIR, reqPath, 'index.html');
        if (fileExists(dirIndexHtmlPath)) {
            return res.redirect(301, `${reqPath}/`);
        }
    }

    next();
});

// Serve static assets (js, css, images, fonts)
app.use(express.static(PUBLIC_DIR));

// Handle 404
app.use((req, res) => {
    res.status(404);
    // Serve custom error page if cloned, otherwise text
    const errorPage = path.join(PUBLIC_DIR, 'en', 'error.html');
    if (fileExists(errorPage)) {
        res.sendFile(errorPage);
    } else {
        res.send('<h1>404 Not Found</h1><p>The page or asset you are looking for does not exist on this cloned site.</p>');
    }
});

app.listen(PORT, () => {
    console.log(`==================================================`);
    console.log(`  West Tours Clone is running locally!`);
    console.log(`  Access the site at: http://localhost:${PORT}/`);
    console.log(`  Press Ctrl+C to stop the server.`);
    console.log(`==================================================`);
});

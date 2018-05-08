
from pyppeteer import launch


async def screenshot(url, img_type='png'):
    # XXX insecure
    browser = await launch({
        'args': ['--no-sandbox', '--disable-setuid-sandbox']
    })
    page = await browser.newPage()
    await page.goto(url, {
        'waitUntil': ['load', 'documentloaded', 'networkidle0']
    })
    await page.setViewport({'width': 1920, 'height': 1080})
    # Wait for 2 extra seconds and hope the page is really loaded then..
    await page.waitFor(2000)
    buf = await page.screenshot({'type': img_type, 'fullPage': True})
    await browser.close()
    return buf

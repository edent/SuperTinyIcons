const expect = require("chai").expect
const fs = require("fs")
const fetch = require("node-fetch")

const svgDir = __dirname + "/../images/svg/"

const files = fs.readdirSync(svgDir)

files.forEach((filename, i) => {
    if (! filename.endsWith(".svg")) {return}
    const filepath = svgDir + filename
    describe(filename, async () => {
        it("should exists", () => {
             expect(fs.existsSync(filepath)).to.be.true
        })

        it("should be under 1KB", () => {
            expect(fs.statSync(filepath).size).to.be.lessThan(1024)
        })

        it("should be validated by the w3c validator", async () => {
            await fetch("https://validator.w3.org/nu/?out=gnu", {
                    method: "POST",
                    body: fs.readFileSync(filepath, "utf8").replace(/aria-label="[^"]+"/g, ""),
                    headers: new fetch.Headers([["Content-Type", "application/xml"]])
                })
                .then(res => (console.log(i + 1, "/", files.length), res))
                .then(res => res.text())
                .then(res => {
                    expect(res).to.be.empty
                })
        })
    })
})

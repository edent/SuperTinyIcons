const expect = require("chai").expect
const fs = require("fs")
const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));

const svgDir = __dirname + "/../images/svg/"
const readme = __dirname + "/../README.md"

const readmeLines = fs.readFileSync(readme).toString().split("\n")
const files = fs.readdirSync(svgDir)

const readmeRegex = new RegExp("<br>(\\d{1,4}) Bytes<\/td>")

files.forEach((filename, i) => {
    if (! filename.endsWith(".svg")) {return}
    const filepath = svgDir + filename
    describe(filename, async () => {
        it("should exists", () => {
            console.log("  ", i + 1, "/", files.length)
            expect(fs.existsSync(filepath)).to.be.true
        })

        it("should be under 1KB", () => {
            expect(fs.statSync(filepath).size).to.be.lessThan(1024)
        })

        it("should be validated by the w3c validator", async () => {
            await fetch("https://validator.w3.org/nu/?out=gnu", {
                    method: "POST",
                    body: fs.readFileSync(filepath, "utf8").replace(/aria-label="[^"]+"/g, ""),
                    headers: {"Content-Type": "application/xml"}
                })
                .then(res => res.text())
                .then(res => {
                    expect(res).to.be.empty
                })
        })
        
        it("should match readme size", () => {
            for(line of readmeLines) {
                if(line.includes("/svg/"+filename+"\" width=\"125\"")) {
                    const size = parseInt(line.match(readmeRegex)[1])
                    expect(fs.statSync(filepath).size).to.equal(size)
                    break
                }
            }
        })
    })

})

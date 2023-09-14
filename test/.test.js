import { describe, expect, test } from 'bun:test'
import { readdirSync, statSync } from 'fs'
import { execFileSync } from 'child_process'
import vnu from 'vnu-jar'

const svgDir = 'images/svg/'


console.log('Getting file sizes from README')

const readmeLines = (await Bun.file('README.md').text()).split('\n')
const readmeRegex = /<td>.*\/svg\/(.*\.svg).*<br>(\d+) bytes/
const fileSizeMap = new Map()

for (const line of readmeLines) {
  const match = readmeRegex.exec(line)
  if (match) {
    const filename = match[1]
    const size = parseInt(match[2])
    fileSizeMap.set(filename, size)
  }
}


console.log('Validating SVGs with the W3C validator (vnu)')

const validationErrorsMap = new Map()

const args = [
  '-jar', vnu,
  '--skip-non-svg',
  '--filterpattern', '.*aria-label.*',
  svgDir
]

try {
  execFileSync('java', args)
} catch (error) {
  const errors = error.message.split('\n').filter(line => line)
  for (const error of errors) {
    const match = /svg\/((.*\.svg).*)/.exec(error)
    if (match) validationErrorsMap.set(match[2], match[1])
  }
}


console.log('Running tests')

const files = readdirSync(svgDir)

files.forEach(filename => {
  if (!filename.endsWith('.svg')) return

  const filesize = statSync(svgDir + filename).size
  const readmesize = fileSizeMap.get(filename)
  fileSizeMap.delete(filename)

  describe(filename, () => {
    test('should be under 1KB', () => {
      expect(filesize).toBeLessThan(1024)
    })

    test('should be included in readme', () => {
      expect(readmesize).toBeNumber()
    })

    test('should match readme size', () => {
      expect(filesize).toBe(readmesize)
    })

    test('should be validated by the w3c validator', () => {
      expect(validationErrorsMap.get(filename)).toBeFalsy()
    })
  })
})

test('all files in readme should exist', () => {
  expect(fileSizeMap).toBeEmpty()
})

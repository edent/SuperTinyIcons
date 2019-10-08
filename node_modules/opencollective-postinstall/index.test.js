jest.mock('./package.json', () => ({
  name: 'testpkg2',
  collective: {url: 'testurl'}
}), {virtual: true});

describe('test all the things', () => {
  const env = global.process.env;
  const console = global.console;
  beforeEach(() => {
    global.console = {log: jest.fn(), warn: global.console.warn};
  });
  afterEach(() => {
    global.process.env = env;
    global.console.log.mockReset();
    global.console = console;
    jest.resetModules();
  });

  describe('outputs the correct values', () => {
    it('when called without args', () =>{
      expect(global.console.log).not.toHaveBeenCalled();
      require('./index');
      expect(global.console.log).toHaveBeenCalledTimes(3);
      expect(global.console.log).toHaveBeenNthCalledWith(1,
        `\u001b[96m\u001b[1mThank you for using testpkg2!\u001b[96m\u001b[1m`
      );
      expect(global.console.log).toHaveBeenNthCalledWith(3,
        `> \u001b[94mtesturl/donate\u001b[0m\n`
      );
    });

    [0, false].forEach(falsy => {
      it(`when Disable is set to ${falsy}`, () => {
        global.process.env = {DISABLE_OPENCOLLECTIVE: falsy};
        expect(global.console.log).not.toHaveBeenCalled();
        require('./index');
        expect(global.console.log).toHaveBeenCalledTimes(3);
      });
    });

    ['notice', 'http', 'timing', 'info', 'verbose', 'silly'].forEach(log => {
      it(`when config_loglevel is set to ${log}`, () => {
        global.process.env = {npm_config_loglevel: log}
        expect(global.console.log).not.toHaveBeenCalled();
        require('./index');
        expect(global.console.log).toHaveBeenCalledTimes(3);
      });
    });
  });
  
  describe('does not show output', () => {
    [1, true].forEach(truthy => {
      it(`when Disable is set to ${truthy}`, () => {
        global.process.env = {DISABLE_OPENCOLLECTIVE: truthy};
        expect(global.console.log).not.toHaveBeenCalled();
        require('./index');
        expect(global.console.log).not.toHaveBeenCalled();
      });
    });

    ['warn', 'error', 'silent'].forEach(log => {
      it(`when npm_config_loglevel is set to ${log}`, () => {
        global.process.env = {npm_config_loglevel: log}
        require('./index');
        expect(global.console.log).not.toHaveBeenCalled();
      });
    });
  });
});
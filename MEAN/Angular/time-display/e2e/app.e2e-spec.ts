import { TimeDisplayPage } from './app.po';

describe('time-display App', () => {
  let page: TimeDisplayPage;

  beforeEach(() => {
    page = new TimeDisplayPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});

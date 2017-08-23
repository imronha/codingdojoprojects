import { QuestionPage } from './app.po';

describe('question App', () => {
  let page: QuestionPage;

  beforeEach(() => {
    page = new QuestionPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!');
  });
});

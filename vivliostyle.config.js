export default {
  title: 'PDF Template Pack',
  author: 'Template Author',
  language: 'en',
  size: '13.333in 7.5in',
  entry: [
    {
      path: 'src/manuscript/pack.md',
      theme: 'src/styles/pack.css',
    },
  ],
  copyAsset: {
    includes: ['src/assets/**/*'],
  },
  workspaceDir: '.vivliostyle',
};

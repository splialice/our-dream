const path = require('path');
const fs = require('fs');

// 自定义 resolve：忽略 Hugo 传入的虚拟 from 路径，
// 直接在项目级 assets/css 与主题级 assets/css 中定位被 @import 的文件，
// 彻底绕开 postcss-import 相对 from 目录解析失败的问题。
module.exports = {
  plugins: [
    require('postcss-import')({
      resolve: function (id, basedir) {
        const candidates = [
          path.resolve(basedir || '', id),
          path.resolve(__dirname, 'assets/css', id),
          path.resolve(__dirname, 'themes/demius/assets/css', id),
        ];
        for (const c of candidates) {
          if (fs.existsSync(c)) return c;
        }
        // 全部不存在时返回一个候选，让错误信息更明确
        return candidates[0];
      },
    }),
  ],
};

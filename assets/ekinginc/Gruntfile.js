/*!
 * Bootstrap's Gruntfile
 * http://getbootstrap.com
 * Copyright 2013-2014 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */

module.exports = function (grunt) {
  'use strict';

  // Force use of Unix newlines
  grunt.util.linefeed = '\n';

  RegExp.quote = function (string) {
    return string.replace(/[-\\^$*+?.()|[\]{}]/g, '\\$&');
  };

  var fs = require('fs');
  var path = require('path');

  // Project configuration.
  grunt.initConfig({

    // Metadata.
    pkg: grunt.file.readJSON('package.json'),
    // NOTE: This jqueryCheck code is duplicated in customizer.js; if making changes here, be sure to update the other copy too.
    jqueryCheck: 'if (typeof jQuery === \'undefined\') { throw new Error(\'Bootstrap\\\'s JavaScript requires jQuery\') }\n\n',

    // Task configuration.
    clean: {
      dist: ['dist']
    },

    copy: {
      bootstrap: {
        expand: true,
        cwd: '../bootstrap/dist/',
        src: '**',
        dest: '../../public/'
      },
      angularjs: {
        expand: true,
        cwd: '../angularjs/',
        src: 'angular.min.js',
        dest: '../../public/js/'
      },
      jquery: {
        expand: true,
        cwd: '../jquery/dist/',
        src: '**',
        dest: '../../public/js/'
      },
      icheck_skins: {
        expand: true,
        cwd: '../jquery-icheck/skins/',
        src: '**',
        dest: '../../public/iCheck/skins/'
      },
      icheck_js: {
        expand: true,
        cwd: '../jquery-icheck/',
        src: 'icheck.min.js',
        dest: '../../public/iCheck/'
      },
      ekinginc: {
        expand: true,
        cwd: 'dist/',
        src: '**',
        dest: '../../public/'
      },
      ekingjs: {
        expand: true,
        cwd: 'js/',
        src: '**',
        dest: '../../public/js/'
      },
      editor: {
        expand: true,
        cwd: '../editor/',
        src: '**',
        dest: '../../public/editor/'
      }

    },

    sed: {
      versionNumber: {
        pattern: (function () {
          var old = grunt.option('oldver');
          return old ? RegExp.quote(old) : old;
        })(),
        replacement: grunt.option('newver'),
        recursive: true
      }
    },
    less: {
      compileCore: {
        files: {
          '../../public/css/eking.css': 'less/eking.less',
          '../../public/css/bootstrap.css': 'less/bootstrap.less'
        }
      }
    },
    cssmin: {
      core: {
        files: {
          '../../public/css/eking.min.css': '../../public/css/eking.css',
          '../../public/css/bootstrap.min.css': '../../public/css/bootstrap.css'
        }
      }
    },
    uglify:{
      options:{
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'//添加banner
      },
      eking:{
        src: 'js/base.js',
        dest: '../../public/js/base.min.js'
      },
        upload:{
            src: 'js/upload.js',  //cityselector
            dest: '../../public/js/upload.min.js'
        },
        move:{
            src: 'js/move.js',
            dest: '../../public/js/move.min.js'
        },
        page:{
            src: 'js/w-page.js',
            dest: '../../public/js/w-page.min.js'
        },
        cityselector:{
            src: 'js/cityselector.js',
            dest: '../../public/js/cityselector.min.js'
        },
        IframeUpload: {
            src: 'js/IframeUpload.js',
            dest: '../../public/js/IframeUpload.min.js'
        },
        validator: {
            src: 'js/validator.js',
            dest: '../../public/js/validator.min.js'
        },
        diagnosis:{
           src: 'js/diagnosis.js',
           dest: '../../public/js/diagnosis.min.js'
        }
    },
    watch: {
      uglify: {
        files: ['<%= uglify.eking.src %>','<%= uglify.upload.src %>','<%= uglify.move.src %>','<%= uglify.page.src %>','<%= uglify.IframeUpload.src %>','<%= uglify.cityselector.src %>'],
        tasks: ['uglify:eking','uglify:upload','uglify:move','uglify:page','uglify:IframeUpload','uglify:cityselector']
      },
      less: {
        files: ['less/*.less'],
        tasks: ['less:compileCore']
      },
      cssmin:{
        files: '../../public/css/eking.css',
        tasks: ['cssmin:core']
      }
    }
  });
  // These plugins provide necessary tasks.
  require('load-grunt-tasks')(grunt, { scope: 'devDependencies' });
  require('time-grunt')(grunt);

  var runSubset = function (subset) {
    return !process.env.TWBS_TEST || process.env.TWBS_TEST === subset;
  };
  var isUndefOrNonZero = function (val) {
    return val === undefined || val !== '0';
  };
  grunt.registerTask('copy-pkg', ['copy:bootstrap', 'copy:jquery','copy:icheck_skins','copy:icheck_js','copy:angularjs','copy:ekingjs','copy:editor']);
  grunt.registerTask('copy-eking', ['copy:ekinginc']);
  grunt.registerTask('less-eking', ['less:compileCore']);
  grunt.registerTask('uglify-eking', ['uglify:eking','uglify:validator','uglify:upload','uglify:move','uglify:page','uglify:IframeUpload','uglify:cityselector']);
  grunt.registerTask('cssmin-eking', ['cssmin:core']);
  grunt.registerTask('default', ['copy-pkg', 'copy-eking', 'less-eking','cssmin-eking', 'uglify-eking']);
};

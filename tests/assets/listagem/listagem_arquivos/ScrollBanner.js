/*
    Movements based on post of Rachel Smith
    https://codepen.io/rachsmith/post/how-to-move-elements-on-scroll-in-a-way-that-doesn-t-suck-too-bad
*/
function ScrollBanner(data) {
    this.containerHeight = data.containerHeight;
    this.positions = data.positions;

    this.prefix = this.prefix();

    this.running = false;
    this.width;
    this.height;
    this.scrollHeight;
    this.scrollOffset = 0;
    this.scrollOffsetLeft = 0;
    this.movingElements = [];
    this.scrollPercent = 0;
    this.debug;

    this.setDebug(data.debug);
    this.debugController = [];
    for (var i = 0; i < this.positions.length; i++) {
        this.debugController[i] = null;
    }
}

ScrollBanner.prototype.start = function () {
    this.running = true
    this.resize();
    this.initMovingElements();
    this.loop();
    window.onscroll = function () {
        this.loop();
    }.bind(this);
    window.addEventListener('resize', this.resize);
}

ScrollBanner.prototype.stop = function () {
    this.running = false;
    window.removeEventListener('resize', this.resize);
}

ScrollBanner.prototype.initMovingElements = function () {
    this.movingElements = []
    for (var i = 0; i < this.positions.length; i++) {
        var el = document.getElementById(this.positions[i].name);
        this.movingElements.push(el);
    }
}

ScrollBanner.prototype.resize = function () {
    this.width = window.innerWidth;
    this.height = window.innerHeight;
    this.scrollHeight = this.containerHeight - this.height;
}

ScrollBanner.prototype.updateElements = function () {
    for (var i = 0; i < this.movingElements.length; i++) {
        var p = this.positions[i];
        for (var j in p.limits) {
            var l = p.limits[j]
            if (this.scrollOffset <= l.limit) {
                if (l.action == 'stay') {
                    if (this.movingElements[i].style['position'] === 'fixed') {
                        this.movingElements[i].style[this.prefix.lowercase + 'Transform'] = 'translate3d(' + (-1 * this.scrollOffsetLeft) + 'px, ' + l.y + 'px, 0px)';
                    } else {
                        this.movingElements[i].style[this.prefix.lowercase + 'Transform'] = 'translate3d(0px, ' + l.y + 'px, 0px)';
                    }
                    if (this.debugController[i] != 'stay') {
                        this.debugController[i] = 'stay';
                        this.log('j:' + j + ' | ' + p.name + ' | offset: ' + this.scrollOffset + ' | limit: ' + l.limit + ' | action: ' + l.action + ' | Y: ' + l.y)
                    }
                } else if (l.action == 'run') {
                    this.movingElements[i].style[this.prefix.lowercase + 'Transform'] = 'translate3d(' + (-1 * this.scrollOffsetLeft) + 'px, ' + (l.y - this.scrollOffset) + 'px, 0px)';
                    if (this.debugController[i] != 'run') {
                        this.debugController[i] = 'run';
                        this.log('j:' + j + ' | ' + p.name + ' | offset: ' + this.scrollOffset + ' | limit: ' + l.limit + ' | action: ' + l.action + ' | Y: ' + l.y)
                    }
                } else {
                    this.movingElements[i].style[this.prefix.lowercase + 'Transform'] = 'translate3d(' + (-1 * this.scrollOffsetLeft) + 'px, ' + l.y + 'px, 0px)';
                    this.log('j:' + j + ' | ' + p.name + ' | offset: ' + this.scrollOffset + ' | limit: ' + l.limit + ' | action: ' + l.action + ' | Y: ' + l.y)
                }
                break;
            }
        }
    }
}

ScrollBanner.prototype.onScroll = function () {
    const originalMargin = 480;
    const decreaseVelocity = 3.33;
    const decreasePercentage = this.scrollPercent * decreaseVelocity;
    const valueToDecrease = originalMargin * decreasePercentage;
    var decreasingMargin = originalMargin - valueToDecrease;

    decreasingMargin = parseInt(decreasingMargin, /*radix*/10);

    const marginTop = decreasingMargin >= 0 ? decreasingMargin : 0;
    this.movingElements[1].style.marginTop = marginTop + 'px';
}

ScrollBanner.prototype.loop = function () {
    if (this.running) {
        this.scrollOffset = window.pageYOffset || window.scrollTop || 0;
        this.scrollPercent = this.scrollOffset / this.scrollHeight || 0;
        this.scrollOffsetLeft = window.pageXOffset || window.scrollLeft || 0;
        this.onScroll()
        this.updateElements();
    }
}

/* prefix detection http://davidwalsh.name/vendor-prefix */
ScrollBanner.prototype.prefix = function () {
    var styles = window.getComputedStyle(document.documentElement, ''),
        pre = (Array.prototype.slice
                .call(styles)
                .join('')
                .match(/-(moz|webkit|ms)-/) || (styles.OLink === '' && ['', 'o'])
        )[1],
        dom = ('WebKit|Moz|MS|O').match(new RegExp('(' + pre + ')', 'i'))[1];
    return {
        dom: dom,
        lowercase: pre == 'moz' ? 'Moz' : pre,
        css: '-' + pre + '-',
        js: pre[0].toUpperCase() + pre.substr(1)
    };
}

ScrollBanner.prototype.setDebug = function (trueOrFalse) {
    this.debug = Boolean(trueOrFalse);
}

ScrollBanner.prototype.enableDebug = function () {
    this.setDebug(true);
}

ScrollBanner.prototype.disableDebug = function () {
    this.setDebug(false);
}

ScrollBanner.prototype.log = function (logString) {
    if (this.debug)
        console.log(logString)
}

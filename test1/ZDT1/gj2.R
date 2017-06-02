a<-read.table('a.txt')
b<-read.table('b.txt')
c<-read.table('c.txt')
d<-read.table('d.txt')

plot(1:500, a$V1, xlab="进化代数", ylab="临时种群非支配解个数", type="l", xlim=c(1, 500), ylim=c(1, 400), main="ZDT1 临时种群非支配解个数变化趋势图")

lines(1:500, b$V1, lty=3, lwd=2.5, col="green")
lines(1:500, c$V1, lty=3, lwd=5, col="blue")
lines(1:500, d$V1, lty=1, lwd=4.5, col="red")

legend.txt<-c("NSGA-II", "对比算法1", "对比算法2", "改进算法1")
legend("topleft", legend=legend.txt, col=c("black", "green", "blue", "red"), lty=c(1, 3, 4, 1), lwd=c(1,2.5,5,4.5), bty="o", cex=0.8)


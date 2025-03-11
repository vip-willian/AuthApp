# 1 符号位：符号位，也就是最高位，始终是0，没有任何意义，因为要是唯一计算机二进制补码中就是负数，0才是正数。
# 2 时间戳：占用41位，记录生成ID的时间戳，精确到毫秒级。
# 3 机器标识：占用10位，用于标识不同的机器。
# 4 计数序列号：占用12位，用于解决同一毫秒内生成多个ID的冲突
import time

# 64 位 id 的划分,通常机器位和数据位各为 5 位
WORKER_ID_BITS = 5  # 机器位
DATACENTER_ID_BITS = 5  # 数据位
SEQUENCE_BITS = 12  # 循环位

# 最大取值计算,计算机中负数表示为他的补码
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)  # 2**5 -1 =31
MAX_DATACENTER_ID = -1 ^ (-1 << DATACENTER_ID_BITS)

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS
DATACENTER_ID_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS + DATACENTER_ID_BITS

# X序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)

# 元年时间戳
EPOCH = 1288834974657


class Snowflake:
    def __init__(self, worker_id, data_center_id):

        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id 值越界')
        if data_center_id > MAX_DATACENTER_ID or data_center_id < 0:
            raise ValueError('datacenter_id 值越界')

        # 机器标识ID
        self.worker_id = worker_id
        # 数据中心ID
        self.data_center_id = data_center_id
        # 计数序列号
        self.sequence = 0
        # 时间戳
        self.last_timestamp = -1

    def _gen_timestamp(self):
        """生成整数时间戳"""
        return int(time.time() * 1000)

    def _wait_for_next_millis(self, last_timestamp):
        """等到下一毫秒"""
        timestamp = self._gen_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self._gen_timestamp()
        return timestamp

    def next_id(self):
        timestamp = self._gen_timestamp()
        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards. Refusing to generate id for %d milliseconds" % abs(
                timestamp - self.last_timestamp))
        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self._wait_for_next_millis(self.last_timestamp)
        else:
            self.sequence = 0

        self.last_timestamp = timestamp
        return ((timestamp - EPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.data_center_id << DATACENTER_ID_SHIFT) | (
                self.worker_id << WORKER_ID_SHIFT) | self.sequence


snowflake = Snowflake(1, 1)

if __name__ == '__main__':
    print(snowflake.next_id())
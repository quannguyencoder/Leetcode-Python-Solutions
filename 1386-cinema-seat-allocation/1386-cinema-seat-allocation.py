from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        # Gom nhóm các ghế bị đặt theo từng hàng dưới dạng Bitmask
        reserved = defaultdict(int)
        for row, col in reservedSeats:
            reserved[row] |= (1 << col)
            
        # Mặc định ban đầu: tất cả các hàng đều trống, mỗi hàng xếp được 2 gia đình
        total_families = 2 * n
        
        # Định nghĩa mặt nạ bit cho 3 khu vực có thể ngồi
        left_mask = 0b0000111100  # Khớp với các ghế: 2, 3, 4, 5
        right_mask = 0b1111000000 # Khớp với các ghế: 6, 7, 8, 9
        mid_mask = 0b0011110000   # Khớp với các ghế: 4, 5, 6, 7
        
        # Chỉ kiểm tra những hàng có ghế bị đặt
        for row_mask in reserved.values():
            # Tạm trừ đi 2 gia đình mặc định của hàng này để tính toán lại
            total_families -= 2
            
            # Kiểm tra xem có thể xếp được gia đình nào không
            if (row_mask & left_mask == 0) and (row_mask & right_mask == 0):
                # Xếp được 2 gia đình ở cả hai bên
                total_families += 2
            elif (row_mask & left_mask == 0) or (row_mask & right_mask == 0) or (row_mask & mid_mask == 0):
                # Không xếp được 2, nhưng còn đủ chỗ trống cho 1 gia đình ở Trái, Phải HOẶC Giữa
                total_families += 1
                
        return total_families
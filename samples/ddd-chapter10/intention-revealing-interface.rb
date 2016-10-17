class Paint
  attr_accessor :v, :r, :y, :b

  def initialize(v, r, y, b)
    self.v = v
    self.r = r
    self.y = y
    self.b = b
  end

  def paint(paint)
    self.v = v + paint.v
    # ごにょごにょ
    # r, b, y に新しい値を代入
  end
end


paint = Paint.new(1, 2, 3, 4)

puts paint.v
